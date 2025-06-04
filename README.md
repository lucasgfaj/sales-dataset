# Analytics - Sales Dataset

Projeto para análise de dados de vendas utilizando Python e MongoDB.

---

## Dataset

O conjunto de dados utilizado neste projeto está disponível em:

[Sales Dataset - Kaggle](https://www.kaggle.com/datasets/shantanugarg274/sales-dataset)

---

## Descrição

Este projeto tem como objetivo construir uma aplicação para análise e previsão de dados de vendas. A partir da importação de um arquivo CSV para um banco de dados MongoDB, realizamos análises exploratórias e preditivas para obter insights valiosos sobre:

- Produtos mais vendidos
- Regiões com maior volume de vendas
- Métodos de pagamento predominantes

---

## Etapas Principais

1. **Ingestão de Dados**  
   Importação do arquivo CSV para o MongoDB, aproveitando a flexibilidade do esquema NoSQL para armazenamento dos dados.

2. **Pré-processamento**  
   Limpeza e transformação dos dados, incluindo conversão de tipos, tratamento de valores faltantes e normalização de campos.

3. **Análise Exploratória**  
   Avaliação de métricas importantes como vendas totais, lucro e volume por produto, região e método de pagamento.

4. **Modelagem Preditiva**  
   Aplicação de modelos para previsão de vendas e recomendações de produtos com base em dados históricos.

5. **Relatórios e Visualizações**  
   Criação de gráficos e relatórios que auxiliam na tomada de decisão, destacando investimentos em produtos e regiões com maior potencial.

---

## Setup e Execução

Instale a Extensão do Jupyter no VScode 

[Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)

Para configurar o ambiente Python, execute os seguintes comandos:

```bash
python3 -m venv .venv
```
```bash
source .venv/bin/activate  # Para Linux/macOS
# .venv\Scripts\activate    # Para Windows PowerShell
```
```bash
python3 dependences.py
```
