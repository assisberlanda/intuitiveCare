import tabula
import pandas as pd
import zipfile
import os
import shutil

def descompactar_zip(caminho_zip, pasta_destino="test_table"):
    """
    Descompacta um arquivo ZIP em uma pasta de destino.

    Args:
        caminho_zip (str): Caminho para o arquivo ZIP.
        pasta_destino (str): Caminho para a pasta onde os arquivos serão extraídos.
    """
    try:
        # Cria a pasta de destino, se não existir
        os.makedirs(pasta_destino, exist_ok=True)
        
        with zipfile.ZipFile(caminho_zip, 'r') as arquivo_zip:
            arquivo_zip.extractall(pasta_destino)
        print(f"Arquivo '{caminho_zip}' descompactado com sucesso em '{pasta_destino}'")
    except FileNotFoundError:
        print(f"Erro: Arquivo '{caminho_zip}' não encontrado.")
    except zipfile.BadZipFile:
        print(f"Erro: Arquivo '{caminho_zip}' não é um arquivo ZIP válido.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

def processar_tabela_pdf(arquivo_pdf, pasta_destino):
    """
    Extrai dados de uma tabela em um arquivo PDF, salva em CSV e compacta em ZIP.

    Args:
        arquivo_pdf (str): Caminho para o arquivo PDF.
        pasta_destino (str): Pasta onde os arquivos serão salvos.
    """
    try:
        # Garante que a pasta de destino existe
        os.makedirs(pasta_destino, exist_ok=True)
        
        # Define os caminhos dos arquivos
        nome_arquivo_csv = os.path.join(pasta_destino, "tabela_procedimentos.csv")
        nome_arquivo_zip = os.path.join(pasta_destino, "Teste_assis_berlanda.zip")
        
        # Extrai tabelas do PDF
        tabelas = tabula.read_pdf(arquivo_pdf, pages='all')

        # Concatena todas as tabelas em um único DataFrame
        df = pd.concat(tabelas, ignore_index=True)

        # Renomeia colunas
        df.rename(columns={'OD': 'Odontologia', 'AMB': 'Ambulatorial'}, inplace=True)

        # Salva o DataFrame em um arquivo CSV
        df.to_csv(nome_arquivo_csv, index=False)

        # Compacta o arquivo CSV em um arquivo ZIP
        with zipfile.ZipFile(nome_arquivo_zip, 'w') as arquivo_zip:
            arquivo_zip.write(nome_arquivo_csv, os.path.basename(nome_arquivo_csv))

        print(f"Arquivo CSV '{nome_arquivo_csv}' criado e compactado com sucesso!")
        
        # Apaga o arquivo CSV após a criação do ZIP
        os.remove(nome_arquivo_csv)
        print(f"Arquivo CSV '{nome_arquivo_csv}' apagado com sucesso!")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def apagar_pasta_e_conteudo(caminho_pasta):
    """
    Apaga uma pasta e todo o seu conteúdo.

    Args:
        caminho_pasta (str): O caminho da pasta a ser apagada.
    """
    try:
        shutil.rmtree(caminho_pasta)
        print(f"Pasta '{caminho_pasta}' e seu conteúdo apagados com sucesso.")
    except FileNotFoundError:
        print(f"Erro: Pasta '{caminho_pasta}' não encontrada.")
    except PermissionError:
        print(f"Erro: Permissão negada para apagar '{caminho_pasta}'.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

# Caminhos dos arquivos e pastas
pasta_principal = '/Users/berlanda/Downloads/intuitiveCare/test_table'
pasta_anexos = os.path.join(pasta_principal, 'anexos')
caminho_zip = '/Users/berlanda/Downloads/intuitiveCare/web_scraping/anexos.zip'
arquivo_pdf = os.path.join(pasta_anexos, 'Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf')

# Garante que a pasta principal existe
os.makedirs(pasta_principal, exist_ok=True)

# Descompacta o arquivo ZIP
descompactar_zip(caminho_zip, pasta_anexos)

# Processa o arquivo PDF e salva o CSV
processar_tabela_pdf(arquivo_pdf, pasta_principal)

# Apaga a pasta anexos e seu conteúdo
apagar_pasta_e_conteudo(pasta_anexos)
