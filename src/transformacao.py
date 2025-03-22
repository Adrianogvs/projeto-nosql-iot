import pandas as pd
from pathlib import Path
import sys
import logging

# Configura logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Definir encoding UTF-8 para evitar erro no Windows
sys.stdout.reconfigure(encoding='utf-8')

# Caminhos
PASTA_PROCESSADOS = Path("/opt/airflow/data/processed/")
CAMINHO_CSV = PASTA_PROCESSADOS / "sensores_extraidos.csv"
CAMINHO_CSV_TRANSFORMADO = PASTA_PROCESSADOS / "sensores_transformados.csv"
CAMINHO_PARQUET_TRANSFORMADO = PASTA_PROCESSADOS / "sensores_transformados.parquet"

def carregar_dados():
    """Carrega o arquivo CSV extraído"""
    if not CAMINHO_CSV.exists():
        logger.error(f"[ERRO] Arquivo {CAMINHO_CSV} não encontrado para transformação.")
        raise FileNotFoundError(f"[ERRO] Arquivo {CAMINHO_CSV} não encontrado!")

    df = pd.read_csv(CAMINHO_CSV)
    logger.info(f"[OK] {df.shape[0]} registros carregados do CSV.")
    return df

def transformar_dados(df):
    """Aplica transformações no DataFrame"""
    df = df.dropna()  # Remove nulos
    df['timestamp'] = pd.to_datetime(df['timestamp'])  # Converte timestamp
    df['tipo_sensor'] = df['tipo_sensor'].str.lower().str.strip()  # Padroniza texto
    df['valor'] = df['valor'].astype(float)  # Garante tipo numérico

    logger.info(f"[OK] Dados transformados com sucesso. Total: {df.shape[0]} linhas.")
    return df

def salvar_dados(df):
    """Salva os dados transformados"""
    df.to_csv(CAMINHO_CSV_TRANSFORMADO, index=False)
    df.to_parquet(CAMINHO_PARQUET_TRANSFORMADO, index=False, engine='pyarrow')

    logger.info(f"[SALVO] CSV transformado: {CAMINHO_CSV_TRANSFORMADO}")
    logger.info(f"[SALVO] Parquet transformado: {CAMINHO_PARQUET_TRANSFORMADO}")

if __name__ == "__main__":
    logger.info("Iniciando transformação dos dados...")
    df_bruto = carregar_dados()
    df_transformado = transformar_dados(df_bruto)
    salvar_dados(df_transformado)
    logger.info("Transformação finalizada com sucesso!")
