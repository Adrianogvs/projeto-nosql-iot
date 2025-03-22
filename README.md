# Projeto NoSQL IoT - Engenharia de Dados com Apache Airflow + Docker

Este projeto simula um caso real da Petrobras: sensores IoT monitoram bombas e compressores em plataformas offshore. Esses dados chegam em JSON, são tratados com Python e orquestrados com Apache Airflow, e salvos como Parquet para análise.

---

## O que você precisa ter instalado?

### 1. [Python 3.12+](https://www.python.org/downloads/)

### 2. [Git](https://git-scm.com/)

### 3. [Docker Desktop](https://www.docker.com/products/docker-desktop/)

### 4. [Visual Studio Code (VSCode)](https://code.visualstudio.com/) (opcional, mas recomendado)

---

## Clonar o projeto

Abra o terminal e digite:

```bash
git clone https://github.com/SEU_USUARIO/projeto-nosql-iot.git
cd projeto-nosql-iot
```

---

## Criar ambiente virtual e instalar as dependências

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
# source .venv/bin/activate   # Linux/macOS

pip install -r airflow/requirements.txt
```

---

## Subir o Apache Airflow com Docker

### 1. Rode os containers:

```bash
docker-compose up -d
```

### 2. Acesse o Airflow no navegador:

```
http://localhost:8080
```

- **Usuário**: `admin`
- **Senha**: `admin`

---

## Estrutura de Pastas

```bash
projeto-nosql-iot/
├── .github/
│   └── workflows/
│       └── python-pipeline.yml         # CI/CD com GitHub Actions
├── airflow/
│   ├── dags/
│   │   └── dag_pipeline.py             # DAG do Airflow
│   ├── logs/                           # Logs do Airflow
│   ├── plugins/                        # Plugins (se necessário)
│   ├── scripts/
│   │   └── gerar_dados_json.py         # Script para gerar JSON simulado
│   └── requirements.txt                # Requisitos do Airflow
├── data/
│   ├── lake/
│   │   └── sensores_lake.parquet       # Arquivo final
│   ├── processed/
│   │   ├── sensores_extraidos.csv
│   │   ├── sensores_extraidos.parquet
│   │   ├── sensores_transformados.csv
│   │   └── sensores_transformados.parquet
│   └── raw/
│       └── sensores_simulados.json     # Dados brutos simulados
├── notebooks/
│   └── exploracao_inicial.ipynb        # Análises exploratórias
├── src/
│   ├── __init__.py
│   ├── carga.py                        # Carrega dados finais
│   ├── extracao.py                     # Extrai dados do JSON
│   ├── pipeline.py                     # Executa pipeline completo
│   └── transformacao.py                # Transforma os dados extraídos
├── tests/
│   └── test_transformacao.py           # Testes unitários da transformação
├── docker-compose.yml                 # Configuração do Docker
└── README.md                          # Documentação principal
```

---

## Executar o pipeline (via Airflow)

1. Acesse o navegador em `http://localhost:8080`
2. Ative a DAG `pipeline_iot_nosql`
3. Clique no botão ▶️ para rodar manualmente
4. Veja o gráfico com as etapas:

---

## Executar manualmente pelo terminal (sem Airflow)

```bash
# Rodar o pipeline completo com Python:
python src/pipeline.py
```

---

## Rodar os testes

```bash
# Windows
$env:PYTHONPATH="." ; pytest tests/

# Linux/macOS
PYTHONPATH=. pytest tests/
```

---

## Prints do Funcionamento

### Docker Desktop com os containers ativos:
![docker](./img/docker_containers.png)

### DAG executada com sucesso no Airflow:
![airflow](./img/airflow_dag_pipeline.png)

---

## Possíveis Evoluções

- Integração com MongoDB Atlas real
- Deploy na nuvem (S3 / Azure Blob)
- Visualização com Streamlit ou Power BI
- Kafka para streaming de dados

---

## Autor

**Adriano Vilela**\
Engenheiro de Dados em formação | Pythonista em construção\
[LinkedIn](https://linkedin.com/in/adrianogvs) • [GitHub](https://github.com/Adrianogvs)

---

Pronto! Agora é só apertar o play na DAG e ver a mágia acontecer!

