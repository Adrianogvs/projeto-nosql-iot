# 🚀 Projeto NoSQL IoT - Engenharia de Dados

[![CI](https://github.com/SEU_USUARIO/projeto-nosql-iot/actions/workflows/python-pipeline.yml/badge.svg)](https://github.com/SEU_USUARIO/projeto-nosql-iot/actions)

Este projeto simula um cenário real da Petrobras, onde sensores IoT monitoram bombas e compressores em plataformas offshore. Os dados são enviados como documentos JSON e armazenados em um banco NoSQL (MongoDB). O pipeline trata, transforma e armazena os dados no formato otimizado (Parquet), pronto para análise.

---

## 📁 Estrutura do Projeto

```bash
projeto-nosql-iot/
├── data/                    # Dados simulados e tratados
│   ├── raw/                # Arquivos JSON gerados (ex: sensores_simulados.json)
│   ├── processed/          # Arquivos intermediários em CSV/Parquet
│   │   ├── sensores_extraidos.csv
│   │   ├── sensores_extraidos.parquet
│   │   ├── sensores_transformados.csv
│   │   └── sensores_transformados.parquet
│   └── lake/               # Resultado final no formato Parquet
│       └── sensores_lake.parquet
│
├── src/                    # Código principal do pipeline
│   ├── extracao.py         # Lê o JSON e transforma em DataFrame
│   ├── transformacao.py    # Limpa, padroniza e transforma os dados
│   ├── carga.py            # Salva os dados no formato final
│   └── pipeline.py         # Executa todas as etapas em sequência
│
├── scripts/                # Scripts utilitários
│   └── gerar_dados_json.py # Geração de dados simulados
│
├── tests/                  # Testes automatizados
│   └── test_transformacao.py # Testa a função de transformação de dados
│
├── dags/                   # (Opcional) DAG para execução no Apache Airflow
│   └── dag_iot_airflow.py
│
├── .github/workflows/      # Configuração do CI/CD com GitHub Actions
│   └── python-pipeline.yml
│
├── requirements.txt        # Dependências do projeto
├── README.md               # Documentação do projeto
└── .env.example            # Exemplo de variáveis de ambiente
```

---

## ⚙️ Tecnologias Utilizadas

- Python 3.12
- MongoDB (estrutura NoSQL simulada)
- Pandas e PyArrow (Parquet)
- Apache Airflow (orquestração)
- Pytest (testes)
- GitHub Actions (CI/CD)

---

## 🧩 Etapas do Pipeline - Passo a Passo

### 1. **Geração de Dados Simulados** (`scripts/gerar_dados_json.py`)
Gera um arquivo JSON com dados de sensores simulando leituras de temperatura, pressão e vibração em plataformas offshore.

```bash
python scripts/gerar_dados_json.py
```

> 📄 Gera o arquivo `data/raw/sensores_simulados.json`

---

### 2. **Extração dos Dados** (`src/extracao.py`)
Carrega o JSON com as leituras e transforma em um DataFrame Pandas, salvando também em CSV e Parquet na pasta `processed`.

```bash
python src/extracao.py
```

> 📁 Salva: `data/processed/sensores_extraidos.csv` e `.parquet`

---

### 3. **Transformação dos Dados** (`src/transformacao.py`)
Aplica as regras de padronização e limpeza:
- Remove nulos
- Converte `timestamp` para datetime
- Padroniza nomes dos sensores
- Converte valores para float

```bash
python src/transformacao.py
```

> 📁 Salva: `data/processed/sensores_transformados.csv` e `.parquet`

---

### 4. **Carga no Data Lake** (`src/carga.py`)
Carrega o arquivo transformado e salva o resultado final no Data Lake local em formato Parquet.

```bash
python src/carga.py
```

> 📁 Salva: `data/lake/sensores_lake.parquet`

---

### 5. **Pipeline Sequencial** (`src/pipeline.py`)
Executa automaticamente as etapas anteriores em sequência.

```bash
python src/pipeline.py
```

---

### 6. **Testes Automatizados** (`tests/test_transformacao.py`)
Testa se a transformação dos dados funciona corretamente, usando dados simulados.

```bash
# Windows
$env:PYTHONPATH="." ; pytest tests/

# Linux/Mac
PYTHONPATH=. pytest tests/
```

---

### 7. **CI/CD com GitHub Actions** (`.github/workflows/python-pipeline.yml`)
Executa automaticamente:
- Instalação das dependências
- Execução do pipeline completo
- Execução dos testes com Pytest

> ✅ Rodado em cada push/pull request na branch `main`

---

## ▶️ Como Executar Localmente

```bash
# Clonar o repositório
git clone https://github.com/SEU_USUARIO/projeto-nosql-iot.git
cd projeto-nosql-iot

# Criar ambiente virtual
python -m venv .venv
.venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt

# Rodar pipeline completo
python src/pipeline.py
```

---

## ✅ Rodar os testes manualmente

```bash
# No Windows (PowerShell)
$env:PYTHONPATH="." ; pytest tests/

# No Linux/Mac
PYTHONPATH=. pytest tests/
```

---

## 🧠 Possíveis Evoluções

- Conectar com MongoDB Atlas real
- Integração com Apache Kafka
- Dashboard com Streamlit
- Salvar Parquet na nuvem (S3, Azure Blob)
- Deploy do Airflow em Docker

---

## 👨‍💻 Autor

**Adriano V. S.**  
Engenheiro de Dados | Pythonista em Construção  
[LinkedIn](https://linkedin.com/in/SEU_USUARIO) • [GitHub](https://github.com/SEU_USUARIO)

