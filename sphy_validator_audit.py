import pandas as pd
import numpy as np
import hashlib
import matplotlib.pyplot as plt
import os

class SPHYValidator:
    def __init__(self, filename='sphy_dataset.parquet'):
        if not os.path.exists(filename):
            raise FileNotFoundError(f"Erro: O arquivo {filename} não foi encontrado.")
        self.filename = filename
        self.df = pd.read_parquet(filename)

    def validate_integrity(self):
        """Re-calcula o SHA256 de cada linha e compara com a assinatura gravada."""
        print(f"--- INICIANDO AUDITORIA DE INTEGRIDADE (SHA256) ---")
        valid_count = 0
        total_rows = len(self.df)

        for i, row in self.df.iterrows():
            # Reconstrói a string bruta exatamente como no gerador original
            raw_string = f"{int(row['frame_id'])}{row['uv_noise_gev']}{row['phi_coherence']}{row['m_higgs_gev']}{row['tensor_strain']}{row['meissner_boost']}"
            recalculated_hash = hashlib.sha256(raw_string.encode()).hexdigest()

            if recalculated_hash == row['sha256_signature']:
                valid_count += 1
            else:
                print(f"ALERTA: Violação de integridade no Frame {i}!")

        integrity_score = (valid_count / total_rows) * 100
        print(f"Resultado: {valid_count}/{total_rows} frames válidos ({integrity_score:.2f}%)")
        return integrity_score == 100

    def generate_metrics(self):
        """Gera as métricas estatísticas de estabilidade física."""
        print("\n--- MÉTRICAS DE ESTABILIDADE FÍSICA ---")
        mean_m = self.df['m_higgs_gev'].mean()
        std_m = self.df['m_higgs_gev'].std()
        max_noise = self.df['uv_noise_gev'].abs().max()
        
        # Coeficiente de Atenuação: Razão entre Ruído UV e Tensão Residual
        attenuation = (self.df['uv_noise_gev'].abs() / self.df['tensor_strain'].abs()).mean()

        print(f"Massa Média de Higgs: {mean_m:.6f} GeV")
        print(f"Desvio Padrão (Estabilidade): {std_m:.8f} GeV")
        print(f"Pico de Estresse UV Processado: {max_noise:.2f} GeV")
        print(f"Fator de Atenuação Geométrica Médio: {attenuation:.2f}x")
        
    def reproduce_plots(self):
        """Recria os gráficos científicos a partir dos dados validados."""
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

        # Plot 1: Estabilidade de Massa sob Ruído
        ax1.scatter(self.df['frame_id'], self.df['uv_noise_gev'], color='gray', alpha=0.1, label='Ruído UV (Input)')
        ax1.plot(self.df['frame_id'], self.df['m_higgs_gev'], color='#00ffcc', label='Massa de Higgs (Output SPHY)')
        ax1.axhline(y=125, color='red', linestyle='--', label='Target (125 GeV)')
        ax1.set_ylabel("Energia / Massa (GeV)")
        ax1.set_title("Reprodutibilidade: Estabilidade da Massa sob Flutuações Quânticas")
        ax1.legend(loc='upper right')

        # Plot 2: Resposta da Coerência (Campo Phi)
        ax2.fill_between(self.df['frame_id'], self.df['phi_coherence'], color='purple', alpha=0.3, label='Campo de Coerência $\Phi$')
        ax2.set_ylabel("Amplitude de Fase $\Phi$")
        ax2.set_xlabel("Frame ID (Evolução Temporal)")
        ax2.legend()

        plt.tight_layout()
        plt.savefig('reproducibility_report.png', dpi=300)
        print("\nGráfico de reprodutibilidade salvo como 'reproducibility_report.png'.")
        plt.show()

# --- Execução do Validador ---
try:
    validator = SPHYValidator('sphy_dataset.parquet')
    if validator.validate_integrity():
        print("CONDIÇÃO VERIFICADA: O dataset é autêntico e não foi violado.")
        validator.generate_metrics()
        validator.reproduce_plots()
    else:
        print("ERRO CRÍTICO: Este dataset foi corrompido ou alterado.")
except Exception as e:
    print(f"Erro na validação: {e}")
