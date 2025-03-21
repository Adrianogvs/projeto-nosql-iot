import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
from src.transformacao import transformar_dados

def test_transformar_dados():
    # Simula dados brutos como se fossem extraídos do CSV
    dados_simulados = pd.DataFrame([
        {
            "plataforma": "P-16",
            "equipamento": "compressor-1",
            "tipo_sensor": "Temperatura",
            "valor": "85.5",
            "unidade": "C",
            "timestamp": "2025-03-21T10:15:00Z"
        },
        {
            "plataforma": "P-40",
            "equipamento": "bomba-2",
            "tipo_sensor": "Pressao",
            "valor": None,
            "unidade": "psi",
            "timestamp": "2025-03-21T10:20:00Z"
        }
    ])

    df_transformado = transformar_dados(dados_simulados)

    # Verifica se só 1 registro válido permaneceu
    assert df_transformado.shape[0] == 1

    # Verifica se os campos foram padronizados
    assert df_transformado["tipo_sensor"].iloc[0] == "temperatura"
    assert isinstance(df_transformado["valor"].iloc[0], float)
    assert pd.api.types.is_datetime64_any_dtype(df_transformado["timestamp"])
