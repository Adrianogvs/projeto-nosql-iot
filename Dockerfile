# Imagem base com Python e dependências
FROM apache/airflow:2.8.1-python3.11

# Define diretório de trabalho
WORKDIR /opt/airflow

# Copia os arquivos do projeto para dentro da imagem
COPY . .

# Instala dependências extras (caso queira usar pandas, pyarrow, etc.)
USER root
RUN pip install --upgrade pip && pip install pandas pyarrow seaborn

# Dá permissão à pasta de logs e scripts
RUN mkdir -p /opt/airflow/logs && chmod -R 777 /opt/airflow

# Volta para o usuário airflow (padrão do container)
USER airflow

# Comando para iniciar o Airflow webserver (você pode customizar)
CMD ["airflow", "standalone"]
