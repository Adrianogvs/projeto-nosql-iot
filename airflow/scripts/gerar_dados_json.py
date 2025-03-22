import json
import random
from datetime import datetime, timezone
from pathlib import Path
import sys
import io

# Força o uso de UTF-8 na saída, se o terminal suportar
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Configurações
NUM_REGISTROS = 1000
TIPOS_SENSORES = ["temperatura", "umidade", "pressao"]
UNIDADES = {"temperatura": "C", "umidade": "%", "pressao": "Pa"}
PLATAFORMAS = ["Plataforma A", "Plataforma B", "Plataforma C"]
EQUIPAMENTOS = ["SensorBox 1", "SensorBox 2", "SensorBox 3"]

# Caminho do arquivo de saída
CAMINHO_ARQUIVO = Path("data/raw/sensores_simulados.json")
CAMINHO_ARQUIVO.parent.mkdir(parents=True, exist_ok=True)

def gerar_registro():
    sensores = []
    agora = datetime.now(timezone.utc).isoformat()

    for tipo in TIPOS_SENSORES:
        sensores.append({
            "tipo": tipo,
            "valor": round(random.uniform(10, 100), 2),
            "unidade": UNIDADES[tipo],
            "timestamp": agora
        })

    return {
        "plataforma": random.choice(PLATAFORMAS),
        "equipamento": random.choice(EQUIPAMENTOS),
        "sensores": sensores
    }

def gerar_dados(num_registros):
    return [gerar_registro() for _ in range(num_registros)]

if __name__ == "__main__":
    dados = gerar_dados(NUM_REGISTROS)

    with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

    print(f"[OK] Arquivo gerado e salvo em {CAMINHO_ARQUIVO}")
