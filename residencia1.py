import os
import shutil
from datetime import datetime

# --- CONFIGURAÇÕES ---
caminho_raiz = r"C:\Users\santoswssf\Desktop\estudo\Dados_Brutos"
arquivo_log = "historico_organizacao.txt"

setores_validos = ["Marketing", "Customer Success", "Financeiro", "Comercial", "Produto", "RH"]

def registrar_log(mensagem):
    """Registra as ações em um arquivo de log externo."""
    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open(arquivo_log, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {mensagem}\n")

def organizar_relatorios():
    """Lê a pasta, identifica o setor e organiza os arquivos."""
    if not os.path.exists(caminho_raiz):
        print(f"\n Erro: O diretório {caminho_raiz} não foi encontrado.")
        return

    arquivos = [f for f in os.listdir(caminho_raiz) if os.path.isfile(os.path.join(caminho_raiz, f))]
    
    print(f"\n--- Iniciando Organização de {len(arquivos)} arquivos ---")
    contagem = 0

    for arquivo in arquivos:
        origem = os.path.join(caminho_raiz, arquivo)
        partes = arquivo.split('_')
        
        # Identificação automática do setor e tratamento de nomes inválidos
        if len(partes) >= 3:
            setor = partes[0]
            nome_pasta = setor if setor in setores_validos else "Outros_Setores"
        else:
            nome_pasta = "Erros_Nomenclatura"

        caminho_destino = os.path.join(caminho_raiz, nome_pasta)
        
        if not os.path.exists(caminho_destino):
            os.makedirs(caminho_destino)

        destino = os.path.join(caminho_destino, arquivo)
        
        try:
            # Tratamento de arquivos duplicados
            if os.path.exists(destino):
                ts = datetime.now().strftime("%H%M%S")
                destino = os.path.join(caminho_destino, f"Copia_{ts}_{arquivo}")

            shutil.move(origem, destino)
            sucesso_msg = f"Movido: {arquivo} -> {nome_pasta}"
            print(f"sucesso {sucesso_msg}")
            registrar_log(sucesso_msg)
            contagem += 1
            
        except Exception as e:
            erro_msg = f"Erro ao mover {arquivo}: {e}"
            print(f"erro {erro_msg}")
            registrar_log(erro_msg)

    print(f"\n--- finalizado {contagem} arquivos processados. ---")

def exibir_logs():
    """Lê e exibe o conteúdo do arquivo de log no terminal."""
    print("\n" + "="*30)
    print("      HISTÓRICO DE LOGS      ")
    print("="*30)
    
    if not os.path.exists(arquivo_log):
        print("Nenhum registro de log encontrado.")
        return
    
    with open(arquivo_log, "r", encoding="utf-8") as f:
        print(f.read())
    print("="*30)

def menu():
    """Painel interativo no terminal."""
    while True:
        print("\n" + "—"*40)
        print("   GESTOR DE RELATÓRIOS CORPORATIVOS   ")
        print("—"*40)
        print("1. Executar Organização Automática")
        print("2. Exibir Logs do Sistema")
        print("0. Sair")
        print("—" * 40)
        
        opcao = input("Selecione uma opção: ")

        if opcao == "1":
            organizar_relatorios()
        elif opcao == "2":
            exibir_logs()
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Escolha 1, 2 ou 0.")

if __name__ == "__main__":
    menu()
