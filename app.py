import streamlit as st
import pandas as pd



st.set_page_config(
    page_title="JRA - Gabriel Barboza",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.sidebar.title(" Navegação")
st.sidebar.markdown("Selecione as opções de análise")

arquivo = "https://drive.google.com/file/d/1Ed9ZfyRHYTnidgectuCNdNjVqoV7AqJ7/view?usp=sharing"

st.sidebar.markdown("---")
st.sidebar.markdown(" **Autor:** Gabriel Barboza")
st.sidebar.markdown(" Projeto JRA")

# ==============================
# Cabeçalho principal
# ==============================
st.title("JRA - Gabriel Barboza")

st.header("Streamlit + parquet + pandas")

st.subheader("Análise de dados da empresa")

st.markdown(
    '''Análise de dados simples, utilizando dos arquivos **parquet** disponíveis.'''
)

st.markdown("---")

# ==============================
# Área principal de análise
# ==============================
st.markdown("## 🔎 Análise Exploratória")

if arquivo:
    df = pd.read_parquet(arquivo)

    st.success("Arquivo carregado com sucesso!")

    st.markdown("###  Estatísticas descritivas do arquivo Parquet estudovendas_2024_03.parquet")
    st.dataframe(df.describe(), use_container_width=True)

# Análise um sobre

else:
    st.info("Carregue um arquivo Parquet para iniciar a análise.")

# ==============================
# Rodapé
# ==============================
st.markdown("---")
st.markdown(
    "<center>© 2026 • Projeto JRA • Desenvolvido com Streamlit</center>",
    unsafe_allow_html=True
)


