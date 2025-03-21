import json
import pandas as pd
from pathlib import Path
import sys

# Definir encoding UTF-8 para evitar erro no Windows
sys.stdout.reconfigure(encoding='utf-8')

# Caminhos dos arquivos
CAMINHO_JSON = Path("data/raw/sensores_simulados.json")
PASTA_PROCESSADOS = Path("data/processed/")
CAMINHO_CSV = PASTA_PROCESSADOS / "sensores_extraidos.csv"
CAMINHO_PARQUET = PASTA_PROCESSADOS / "sensores_extraidos.parquet"

def carregar_dados():
    """Lê o arquivo JSON e retorna os dados como uma lista de dicionários."""
    if not CAMINHO_JSON.exists():
        raise FileNotFoundError(f"[ERRO] Arquivo {CAMINHO_JSON} não encontrado!")

    with open(CAMINHO_JSON, "r", encoding="utf-8") as f:
        dados = json.load(f)
    
    print(f"[OK] {len(dados)} registros carregados do JSON.")
    return dados

def converter_para_dataframe(dados):
    """Transforma os dados carregados em um DataFrame Pandas."""
    registros = []
    
    for doc in dados:
        for sensor in doc["sensores"]:
            registros.append({
                "plataforma": doc["plataforma"],
                "equipamento": doc["equipamento"],
                "tipo_sensor": sensor["tipo"],
                "valor": sensor["valor"],
                "unidade": sensor["unidade"],
                "timestamp": sensor["timestamp"]
            })
    
    df = pd.DataFrame(registros)
    print(f"[OK] DataFrame criado com {df.shape[0]} linhas e {df.shape[1]} colunas.")
    return df

def salvar_dataframe(df):
    """Salva o DataFrame extraído em CSV e Parquet para análise futura."""
    PASTA_PROCESSADOS.mkdir(parents=True, exist_ok=True)
    
    df.to_csv(CAMINHO_CSV, index=False)
    df.to_parquet(CAMINHO_PARQUET, index=False)
    
    print(f"[SALVO] Arquivo CSV: {CAMINHO_CSV}")
    print(f"[SALVO] Arquivo Parquet: {CAMINHO_PARQUET}")

if __name__ == "__main__":
    # Executando o fluxo de extração e salvamento
    dados_json = carregar_dados()
    df_sensores = converter_para_dataframe(dados_json)
    salvar_dataframe(df_sensores)
