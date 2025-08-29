import pandas as pd
import plotly.express as px
import streamlit as st
import os
from datetime import datetime

# Configuração de visualização
st.set_page_config(page_title="Dashboard Covid-19", layout="wide")
st.title("Análise sobre a Covid-19 no Brasil 2020/2022")

# Carregar dados
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
file_path = os.path.join(BASE_DIR, "data", "clean_caso_full.csv")
df = pd.read_csv(file_path)

# Converter coluna de data para datetime
df['data'] = pd.to_datetime(df['data'])

# SIDEBAR
st.sidebar.markdown("<h1 style='text-align: center;'> Filtros </h1>", unsafe_allow_html=True)
st.sidebar.markdown("---")

# Filtro de período
st.sidebar.subheader("Filtro por Período")
min_date = df['data'].min().date()
max_date = df['data'].max().date()

date_range = st.sidebar.date_input(
    "Selecione o período",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

# Filtro de estados
st.sidebar.subheader("Estados")
states_available = sorted(df["estado"].unique())
states_select = st.sidebar.multiselect(
    'Selecione um ou mais estados', 
    states_available, 
    default=states_available
)

st.sidebar.markdown("---")

# Aplicar filtros
if len(date_range) == 2:
    start_date, end_date = date_range
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)
    
    # Filtrar por data e estados
    filtered_df = df[
        (df['data'] >= start_date) & 
        (df['data'] <= end_date) &
        (df['estado'].isin(states_select)) 
    ]
else:
    # Filtrar apenas por estados
    filtered_df = df[(df['estado'].isin(states_select))]
    st.sidebar.warning("Selecione um intervalo de datas válido")

# Verificar se há dados após a filtragem
if filtered_df.empty or len(states_select) == 0:
    st.warning("⚠️ Nenhum dado disponível para os filtros selecionados. Por favor, ajuste os filtros.")
else:
    # Mostrar estatísticas gerais
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        total_casos = filtered_df['confirmados_acumulados'].max()
        st.metric("Total de Casos", f"{total_casos:,.0f}")

    with col2:
        total_obitos = filtered_df['óbitos_acumulados'].max()
        st.metric("Total de Óbitos", f"{total_obitos:,.0f}")

    with col3:
        taxa_letalidade = (total_obitos / total_casos * 100) if total_casos > 0 else 0
        st.metric("Taxa de Letalidade", f"{taxa_letalidade:.2f}%")

    with col4:
        media_movel = filtered_df['novos_casos'].mean()
        st.metric("Média Móvel de Casos", f"{media_movel:.0f}")

    # Gráfico de evolução temporal
    st.subheader("Evolução Temporal de Casos e Óbitos ao Longo do Tempo")
    
    # Agrupar dados por data
    dados_agrupados = filtered_df.groupby('data').agg({
        'novos_casos': 'sum',
        'novos_óbitos': 'sum'
    }).reset_index()
    
    # Criar gráfico apenas se houver dados
    if not dados_agrupados.empty:
        fig = px.line(
            dados_agrupados,
            x='data',
            y=['novos_casos', 'novos_óbitos'],
            labels={'value': 'Quantidade', 'variable': 'Tipo', 'data': 'Data'},
        )

        # Personalizar o hover do gráfico de linha
        if len(fig.data) >= 2: # type: ignore
            # Primeiro trace (novos_casos)
            fig.data[0].hovertemplate = (
                '<b>Data</b>: %{x}<br>'
                '<b>Novos Casos</b>: %{y}<br>'
                '<extra></extra>'
            )

            # Segundo trace (novos_óbitos)
            fig.data[1].hovertemplate = (
                '<b>Data</b>: %{x}<br>'
                '<b>Novos Óbitos</b>: %{y}<br>'
                '<extra></extra>'
            )
            
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("Dados insuficientes para criar o gráfico de evolução temporal.")

    # Gráfico de barras por estado
    st.subheader("Total de Casos Confirmados por Estado")
    
    # Agrupar dados por estado
    casos_por_estado = filtered_df.groupby('estado')['confirmados_acumulados'].max().reset_index()
    casos_por_estado = casos_por_estado.sort_values('confirmados_acumulados', ascending=False)
    
    # Criar gráfico apenas se houver dados
    if not casos_por_estado.empty:
        fig = px.bar(
            casos_por_estado,
            x='estado',
            y='confirmados_acumulados',
            labels={'estado': 'Estado', 'confirmados_acumulados': 'Casos Confirmados'},
        )

        fig.update_traces(
            hovertemplate=(
                '<b>Estado</b>: %{x}<br>'
                '<b>Casos Confirmados</b>: %{y}<br>'
                '<extra></extra>'
            )
        )

        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Dados insuficientes para criar o gráfico de barras por estado.")

    # Gráfico de dispersão por estado
    st.subheader("Distribuição de Casos por Estado (Tamanho proporcional ao número de casos)")
    
    # Criar gráfico apenas se houver dados
    if not casos_por_estado.empty:
        fig = px.scatter(
            casos_por_estado,
            x='estado',
            y='confirmados_acumulados',
            size='confirmados_acumulados',
            color='confirmados_acumulados',
            labels={'estado': 'Estado', 'confirmados_acumulados': 'Casos Confirmados'},
        )

        fig.update_traces(
            hovertemplate=(
                '<b>Estado</b>: %{x}<br>'
                '<b>Casos Confirmados</b>: %{y}<br>'
                '<extra></extra>'
            )
        )

        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Dados insuficientes para criar o gráfico de dispersão.")

# Fonte dos dados (sempre visível, independente dos filtros)
st.markdown("---")
st.markdown("**Fonte:** [Brasil.io - Dataset COVID19](https://brasil.io/dataset/covid19/caso_full/)")