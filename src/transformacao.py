import pandas as pd
from pathlib import Path
import sys

# Evitar problemas de codificação no Windows
sys.stdout.reconfigure(encoding='utf-8')

# Caminhos dos arquivos
PASTA_PROCESSADOS = Path("data/processed/")
CAMINHO_CSV = PASTA_PROCESSADOS / "sensores_extraidos.csv"
CAMINHO_PARQUET = PASTA_PROCESSADOS / "sensores_extraidos.parquet"
CAMINHO_CSV_TRANSFORMADO = PASTA_PROCESSADOS / "sensores_transformados.csv"
CAMINHO_PARQUET_TRANSFORMADO = PASTA_PROCESSADOS / "sensores_transformados.parquet"

def carregar_dados():
    """Carrega os dados extraídos do CSV para um DataFrame."""
    if not CAMINHO_CSV.exists():
        raise FileNotFoundError(f"[ERRO] Arquivo {CAMINHO_CSV} não encontrado!")

    df = pd.read_csv(CAMINHO_CSV)
    print(f"[OK] Dados carregados: {df.shape[0]} linhas, {df.shape[1]} colunas.")
    return df

def transformar_dados(df):
    """Aplica regras de transformação e limpeza no DataFrame."""
    
    # Remover registros com valores nulos
    df.dropna(inplace=True)

    # Padronizar os nomes dos sensores para minúsculas
    df["tipo_sensor"] = df["tipo_sensor"].str.lower()

    # Converter valores para float
    df["valor"] = pd.to_numeric(df["valor"], errors="coerce")

    # Transformar o timestamp em formato datetime
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

    # Remover registros inválidos
    df.dropna(subset=["valor", "timestamp"], inplace=True)

    print(f"[OK] Transformação aplicada: {df.shape[0]} registros finais.")
    return df

def salvar_dados_transformados(df):
    """Salva o DataFrame transformado em CSV e Parquet."""
    PASTA_PROCESSADOS.mkdir(parents=True, exist_ok=True)

    df.to_csv(CAMINHO_CSV_TRANSFORMADO, index=False)
    df.to_parquet(CAMINHO_PARQUET_TRANSFORMADO, index=False)

    print(f"[SALVO] Arquivo CSV: {CAMINHO_CSV_TRANSFORMADO}")
    print(f"[SALVO] Arquivo Parquet: {CAMINHO_PARQUET_TRANSFORMADO}")

if __name__ == "__main__":
    # Executando a transformação
    df_bruto = carregar_dados()
    df_tratado = transformar_dados(df_bruto)
    salvar_dados_transformados(df_tratado)
