# SPHY Framework: Estabilização Gravitacional da Massa de Higgs

Este repositório contém o ecossistema computacional e o dataset experimental que fundamentam o artigo **"Dinâmica Hamiltoniana e Coerência de Fase SPHY: Uma Solução para a Instabilidade de Massa"**.

O objetivo deste projeto é demonstrar, via simulação Hamiltoniana, como a coerência de fase da geometria quântica (SPHY) atua como um mecanismo de *screening* (blindagem) para proteger a massa do Higgs de divergências radiativas UV.

## 📊 Resultados em Destaque
* **Fator de Atenuação:** 22.517x (Redução do ruído UV vs. Massa estável).
* **Eficiência de Blindagem:** 79,79%.
* **Drift de Massa:** < 0.01 GeV (Convergência de Lyapunov).
* **Integridade:** 100% dos dados validados via SHA256.

---

## 📂 Estrutura do Repositório

### 1. Dataset de Pesquisa
* **`sphy_dataset.parquet`**: Dataset principal contendo 5.000 frames de evolução temporal. O formato Parquet garante alta performance e preservação de metadados. Cada entrada possui uma assinatura digital SHA256 para garantir que a física não foi alterada.

### 2. Validadores e Auditoria (Scripts Python)
* **`sphy_validator_audit.py`**: O "Tribunal de Integridade". Este script lê o arquivo Parquet, recalcula os hashes SHA256 de cada frame e valida se os dados são autênticos. Também gera as métricas estatísticas de atenuação.
* **`sphy_flow_topology_validator.py`**: Analisa a convergência Hamiltoniana. Ele prova matematicamente que o sistema atinge um atrator estável (estabilidade de Lyapunov) em 125 GeV.

### 3. Provas Visuais (Gráficos Gerados)
* **`atrator_fase.png`**: Representação no espaço de fase ($\Phi$ vs $\Pi_\Phi$) mostrando a trajetória de estabilização.
* **`reproducibility_report.png`**: Gráfico comparativo entre o ruído UV de entrada e a estabilidade da massa de saída.
* **`sphy_topology_analysis.png`**: Histograma de distribuição de massa e mapeamento de eficiência do tensor.
* **`assinatura_tensor.png`**: Visualização do acoplamento entre a coerência de fase e a tensão reduzida do espaço-tempo.

---

## 🚀 Como Reproduzir os Resultados

Para validar a integridade da pesquisa em sua máquina local (Recomendado: Linux/Pop!_OS):

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/deywe/tenso_higgs_sphy.git](https://github.com/deywe/tenso_higgs_sphy.git)
   cd tenso_higgs_sphy
Instale as dependências:

Bash
pip install pandas pyarrow matplotlib numpy
Execute a Auditoria de Integridade:

Bash
python3 sphy_validator_audit.py
Execute a Análise Topológica:

Bash
python3 sphy_flow_topology_validator.py
📜 Citação
Se este modelo ou dataset for útil para sua pesquisa, por favor cite:
Okabe, D. (2026). Dinâmica Hamiltoniana e Coerência de Fase SPHY: Uma Solução para a Instabilidade de Massa.

Harpia Quantum Brasil - Explorando a fronteira da coerência gravitacional.
