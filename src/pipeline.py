import subprocess

def executar_script(script):
    """Executa um script Python como subprocesso e verifica se houve erro."""
    print(f"🔄 Executando: {script}")
    resultado = subprocess.run(["python", script], capture_output=True, text=True)

    if resultado.returncode == 0:
        print(f"✅ {script} executado com sucesso!")
        print(resultado.stdout)  # Exibe a saída do script
    else:
        print(f"❌ Erro ao executar {script}!")
        print(resultado.stderr)  # Exibe o erro
        exit(1)

if __name__ == "__main__":
    print("🚀 Iniciando Pipeline de Dados NoSQL")

    # Passo 1: Gerar os dados simulados
    executar_script("scripts/gerar_dados_json.py")

    # Passo 2: Extrair os dados do JSON
    executar_script("src/extracao.py")

    # Passo 3: Transformar os dados
    executar_script("src/transformacao.py")

    # Passo 4: Carregar os dados no Data Lake
    executar_script("src/carga.py")

    print("🎯 Pipeline concluído com sucesso!")
