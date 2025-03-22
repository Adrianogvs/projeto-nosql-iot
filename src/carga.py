import pandas as pd
from pathlib import Path
import sys

# Corrige o encoding do terminal para evitar erro com Unicode
sys.stdout.reconfigure(encoding='utf-8')

# Caminhos das pastas e arquivos
PASTA_PROCESSED = Path("/opt/airflow/data/processed/")
PASTA_LAKE = Path("data/lake/")

CAMINHO_CSV_TRANSFORMADO = PASTA_PROCESSED / "sensores_transformados.csv"
CAMINHO_PARQUET_LAKE = PASTA_LAKE / "sensores_lake.parquet"

def carregar_dados_transformados():
    """Carrega os dados transformados do CSV para um DataFrame."""
    if not CAMINHO_CSV_TRANSFORMADO.exists():
        raise FileNotFoundError(f"[ERRO] Arquivo {CAMINHO_CSV_TRANSFORMADO} não encontrado!")

    df = pd.read_csv(CAMINHO_CSV_TRANSFORMADO)
    print(f"[OK] Dados transformados carregados: {df.shape[0]} registros.")
    return df

def salvar_no_data_lake(df):
    """Salva o DataFrame no formato Parquet no Data Lake."""
    PASTA_LAKE.mkdir(parents=True, exist_ok=True)
    
    df.to_parquet(CAMINHO_PARQUET_LAKE, index=False)
    print(f"[SALVO] Arquivo Parquet salvo no Data Lake: {CAMINHO_PARQUET_LAKE}")

if __name__ == "__main__":
    # Executar a carga
    df_final = carregar_dados_transformados()
    salvar_no_data_lake(df_final)
