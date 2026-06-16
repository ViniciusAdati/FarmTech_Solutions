import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

load_dotenv()

usuario = os.getenv("DB_USER") or os.getenv("ORACLE_USER")
senha = os.getenv("DB_PASS") or os.getenv("ORACLE_PASSWORD")
host = os.getenv("DB_HOST") or os.getenv("ORACLE_HOST")
porta = os.getenv("DB_PORT") or os.getenv("ORACLE_PORT")
servico = os.getenv("DB_SERVICE") or os.getenv("ORACLE_SERVICE_NAME")

url_banco = f"oracle+oracledb://{usuario}:{senha}@{host}:{porta}/?service_name={servico}"

print("Conectando ao banco Oracle da FIAP...")

try:
    engine = create_engine(url_banco)
    df = pd.read_sql_query('SELECT * FROM "SENSORES"', engine)
    print(f"Sucesso! {len(df)} linhas carregadas do banco de dados.")
except Exception as e:
    print(f"Erro ao conectar no banco: {e}")
    exit()

if len(df) < 20:
    print("Aviso: O banco tem poucos dados para um treinamento ideal.")
df.columns = df.columns.str.upper()

colunas_numericas = ['UMIDADE_SOLO', 'PH', 'NITROGENIO', 'FOSFORO', 'POTASSIO', 'VAI_CHOVER', 'BOMBA_LIGADA']

for col in colunas_numericas:
    if col in df.columns:
        temp = df[col].astype(str)
        temp = temp.str.strip()
        temp = temp.replace({'True': '1', 'False': '0', 'true': '1', 'false': '0'})
        temp = temp.str.replace(',', '.')
        df[col] = temp.astype(float)

df.fillna(df.mean(numeric_only=True), inplace=True)

X = df[['UMIDADE_SOLO', 'PH', 'NITROGENIO', 'FOSFORO', 'POTASSIO', 'VAI_CHOVER']]
y = df['BOMBA_LIGADA']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Treinando o modelo de Regressão Linear...")
modelo = LinearRegression()
modelo.fit(X_train, y_train)

previsoes = modelo.predict(X_test)

mae = mean_absolute_error(y_test, previsoes)
mse = mean_squared_error(y_test, previsoes)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, previsoes)

print("\n--- MÉTRICAS DE DESEMPENHO ---")
print(f"MAE (Erro Absoluto Médio): {mae:.4f}")
print(f"MSE (Erro Quadrático Médio): {mse:.4f}")
print(f"RMSE (Raiz do Erro Quadrático Médio): {rmse:.4f}")
print(f"R² (Coeficiente de Determinação): {r2:.4f}")

joblib.dump(modelo, 'modelo_irrigacao.pkl')
print("\nModelo exportado com sucesso como 'modelo_irrigacao.pkl'!")