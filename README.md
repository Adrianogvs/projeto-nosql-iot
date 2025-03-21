# projeto-nosql-iot
# Projeto NoSQL - Sensores IoT Offshore (MongoDB + Python + Airflow)

Este projeto simula um cenário real da Petrobras, com dados de sensores instalados em compressores e bombas de plataformas offshore. Os dados são armazenados em um banco **NoSQL (MongoDB)** e tratados por uma pipeline em **Python**, orquestrada com **Apache Airflow**, com entrega final em **formato Parquet** para consumo por analistas e cientistas de dados.

---

## 📌 Objetivos

- Armazenar e manipular dados NoSQL (JSON) em MongoDB.
- Transformar dados semi-estruturados em estrutura tabular.
- Criar uma pipeline ETL (extração, transformação e carga).
- Orquestrar o processo com Airflow.
- Preparar os dados para consumo no Power BI / Streamlit.
- Simular um ambiente CI/CD com GitHub Actions.

---

## 🏗️ Estrutura

```bash
projeto-nosql-iot/
│
├── README.md
├── requirements.txt
├── .env
├── .gitignore
│
├── data/
│   └── raw/
│       └── sensores_simulados.json
│
├── notebooks/
│   └── exploracao_inicial.ipynb
│
├── src/
│   ├── __init__.py
│   ├── extracao.py
│   ├── transformacao.py
│   ├── carga.py
│   └── pipeline.py
│
├── dags/
│   └── dag_iot_airflow.py
│
├── docker/
│   └── docker-compose.yml
│
├── scripts/
│   └── gerar_dados_json.py
│
└── tests/
    └── test_transformacao.py
```