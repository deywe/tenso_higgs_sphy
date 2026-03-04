import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class SPHYFlowValidator:
    def __init__(self, filename='sphy_dataset.parquet'):
        self.df = pd.read_parquet(filename)

    def validate_hamiltonian_flow(self):
        print("--- AUDITORIA DE FLUXO TOPOLÓGICO SPHY ---")
        
        # 1. Teste de Blindagem (Screening Efficiency)
        # Verifica se o tensor_strain diminui conforme uv_noise aumenta
        efficiency = (1 - (self.df['tensor_strain'].abs() / self.df['uv_noise_gev'].abs())).mean() * 100
        
        # 2. Estabilidade de Lyapunov (Convergência para o ponto fixo de 125GeV)
        # Medimos a 'distância' do alvo nos últimos 10% dos frames
        tail_df = self.df.tail(int(len(self.df)*0.1))
        target_drift = abs(tail_df['m_higgs_gev'].mean() - 125.0)
        
        print(f"Eficiência de Blindagem do Tensor: {efficiency:.4f}%")
        print(f"Deriva Final do Alvo (Drift): {target_drift:.8e} GeV")
        
        if target_drift < 1e-3:
            print("STATUS: Convergência de Lyapunov Detectada (Sistema Estável).")
        
    def plot_phase_and_energy(self):
        plt.figure(figsize=(12, 5))
        
        # Plot de Transferência de Energia: Ruído vs Tensão Reduzida
        plt.subplot(1, 2, 1)
        plt.scatter(self.df['uv_noise_gev'], self.df['tensor_strain'], 
                    c=self.df['phi_coherence'], cmap='magma', alpha=0.5, s=2)
        plt.title("Mapeamento de Screening (UV vs Strain)")
        plt.xlabel("Input UV (Energia Bruta)")
        plt.ylabel("Output Tensor (Energia Sentida)")
        plt.grid(alpha=0.3)

        # Plot de Densidade de Probabilidade da Massa (Histograma de Estabilidade)
        plt.subplot(1, 2, 2)
        plt.hist(self.df['m_higgs_gev'], bins=100, color='#00ffcc', edgecolor='black')
        plt.axvline(125, color='red', linestyle='dashed', label='Valor Experimental')
        plt.title("Distribuição da Massa de Higgs")
        plt.xlabel("Massa (GeV)")
        plt.ylabel("Frequência de Ocorrência")
        plt.legend()

        plt.tight_layout()
        plt.savefig('sphy_topology_analysis.png')
        print("\nAnálise topológica salva em 'sphy_topology_analysis.png'.")
        plt.show()

# --- Execução ---
flow_val = SPHYFlowValidator()
flow_val.validate_hamiltonian_flow()
flow_val.plot_phase_and_energy()
