
# Análise de Dados da COVID-19 no Brasil

## Link para visualização

Streamlit.io: 

## Descrição

Este projeto consiste em um dashboard interativo para análise de dados da COVID-19 no Brasil, abrangendo o período de 2020 a 2022. A aplicação foi desenvolvida com Streamlit e permite a visualização de casos, óbitos e outros indicadores através de gráficos e métricas dinâmicas.

## Features

- Dashboard interativo com filtros por período e estado.
- Visualização de dados em tempo real (baseado no dataset).
- Gráficos de evolução temporal de casos e óbitos.
- Gráfico de barras com o total de casos confirmados por estado.
- Gráfico de dispersão para distribuição de casos por estado.
- Métricas chave: Total de Casos, Total de Óbitos, Taxa de Letalidade e Média Móvel de Casos.

## Fonte dos Dados

Os dados brutos utilizados neste projeto são provenientes do [Brasil.io](https://brasil.io/dataset/covid19/caso_full/), que compila dados dos boletins das secretarias estaduais de saúde.

**Observação:** Os arquivos CSV não estão incluídos neste repositório devido ao seu tamanho. É necessário baixar o arquivo `caso_full.csv` da fonte mencionada e colocá-lo em um diretório `data/` na raiz do projeto.

## Começando

Siga as instruções abaixo para configurar e executar o projeto em seu ambiente local.

### Pré-requisitos

- Python 3.8 ou superior

### Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```
2. **Crie e ative um ambiente virtual:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
   ```
3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. **Prepare os dados:**

   - Crie uma pasta chamada `data` na raiz do projeto.
   - Baixe o arquivo `caso_full.csv` do [Brasil.io](https://brasil.io/dataset/covid19/caso_full/).
   - Coloque o arquivo `caso_full.csv` dentro da pasta `data`.
2. **Execute o script de limpeza de dados:**
   Este script irá processar o arquivo `caso_full.csv` e gerar o `clean_caso_full.csv` que é utilizado pelo dashboard.

   ```bash
   python src/config.py
   ```
3. **Execute a aplicação Streamlit:**

   ```bash
   streamlit run src/main.py
   ```

   A aplicação será aberta em seu navegador padrão.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Streamlit**: Framework para criação de aplicações web de dados.
- **Pandas**: Biblioteca para manipulação e análise de dados.
- **Plotly**: Biblioteca para criação de gráficos interativos.
- **Jupyter Notebook**: Para exploração inicial dos dados.
