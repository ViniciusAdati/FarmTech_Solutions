import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import joblib
import numpy as np
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="FarmTech - IA Agrícola", layout="wide", page_icon="🌾")
st.title("🌾 FarmTech Solutions: Assistente Agrícola Inteligente")

@st.cache_data(ttl=10) 
def carregar_dados():
    usuario = os.getenv("DB_USER")
    senha = os.getenv("DB_PASS")
    host = os.getenv("DB_HOST")
    porta = os.getenv("DB_PORT")
    servico = os.getenv("DB_SERVICE")
    
    url_banco = f"oracle+oracledb://{usuario}:{senha}@{host}:{porta}/?service_name={servico}"
    
    try:
        engine = create_engine(url_banco)
        query = 'SELECT * FROM "SENSORES" ORDER BY TIMESTAMP DESC FETCH FIRST 100 ROWS ONLY'
        df = pd.read_sql_query(query, engine)
        df.columns = df.columns.str.upper()
        
        colunas_numericas = ['UMIDADE_SOLO', 'PH', 'NITROGENIO', 'FOSFORO', 'POTASSIO', 'VAI_CHOVER', 'BOMBA_LIGADA']
        for col in colunas_numericas:
            if col in df.columns:
                temp = df[col].astype(str).str.strip()
                temp = temp.replace({'True': '1', 'False': '0', 'true': '1', 'false': '0'})
                temp = temp.str.replace(',', '.')
                df[col] = temp.astype(float)
                
        return df
    except Exception as e:
        st.error(f"Erro de conexão com o banco Oracle: {e}")
        return pd.DataFrame()
    
try:
    modelo = joblib.load('modelo_irrigacao.pkl')
    modelo_carregado = True
except FileNotFoundError:
    modelo_carregado = False

aba_dashboard, aba_simulador = st.tabs(["📊 Dashboard Analítico", "🤖 Previsão Interativa (IA)"])

with aba_dashboard:
    st.header("Monitoramento em Tempo Real - Nuvem FIAP")
    df_sensores = carregar_dados()
    
    if not df_sensores.empty:
        st.dataframe(df_sensores.head(10), use_container_width=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Tendência de Umidade do Solo")
            if 'TIMESTAMP' in df_sensores.columns:
                df_linha = df_sensores[['TIMESTAMP', 'UMIDADE_SOLO']].set_index('TIMESTAMP')
                st.line_chart(df_linha)
            else:
                st.line_chart(df_sensores['UMIDADE_SOLO'])
                
        with col2:
            st.subheader("Correlação: Umidade vs Tempo de Bomba")
            st.scatter_chart(df_sensores, x='UMIDADE_SOLO', y='BOMBA_LIGADA')
    else:
        st.warning("Nenhum dado encontrado ou tabela vazia no momento.")

with aba_simulador:
    st.header("Simulador de Manejo Agrícola")
    
    if modelo_carregado:
        st.write("Insira as condições atmosféricas e do solo na barra lateral para gerar uma recomendação autônoma da IA.")
        st.sidebar.header("Parâmetros do Campo")
        sim_umidade = st.sidebar.slider("Umidade do Solo (%)", 0.0, 100.0, 30.0)
        sim_ph = st.sidebar.slider("Nível de pH", 0.0, 14.0, 6.5)
        sim_n = st.sidebar.slider("Nitrogênio (NPK)", 0, 100, 20)
        sim_p = st.sidebar.slider("Fósforo (NPK)", 0, 100, 20)
        sim_k = st.sidebar.slider("Potássio (NPK)", 0, 100, 20)
        sim_chuva = st.sidebar.radio("Previsão de Chuva nas próximas 24h?", ["Não", "Sim"])
        
        val_chuva = 1 if sim_chuva == "Sim" else 0

        if st.sidebar.button("Gerar Recomendação da IA"):
            array_entrada = np.array([[sim_umidade, sim_ph, sim_n, sim_p, sim_k, val_chuva]])
            
            previsao = modelo.predict(array_entrada)[0]
            
            st.subheader("Diagnóstico e Ação Recomendada")
            if previsao > 15 and sim_umidade < 50:
                st.error("🚨 Alerta: Necessidade de Irrigação Detectada")
                st.write(f"**Ação Operacional:** Acionar bomba de irrigação por aproximadamente **{previsao:.0f} minutos**.")
            else:
                st.success("✅ Condições Hídricas Ideais")
                st.write("**Ação Operacional:** Nenhuma intervenção necessária. Solo com saturação adequada.")
    else:
        st.error("⚠️ Modelo preditivo não encontrado! Execute `python modelo.py` no terminal primeiro para treinar e exportar a inteligência artificial.")