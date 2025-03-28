import requests
from bs4 import BeautifulSoup
import zipfile
import os

def baixar_e_compactar_anexos(url, pasta_destino="web_scraping"):
    """
    Baixa os anexos I e II em PDF do site especificado e os compacta em um arquivo ZIP.

    Args:
        url (str): A URL do site contendo os links para os anexos.
        pasta_destino (str): A pasta onde os anexos serão salvos e o arquivo ZIP será criado.
    """

    try:
        # 1. Acessa o site
        response = requests.get(url)
        response.raise_for_status()  # Lança uma exceção para erros HTTP

        # 2. Extrai os links dos anexos
        soup = BeautifulSoup(response.content, "html.parser")
        links_anexos = [a["href"] for a in soup.find_all("a") if "Anexo" in a.text and a["href"].endswith(".pdf")]

        # Cria a pasta de destino, se não existir
        os.makedirs(pasta_destino, exist_ok=True)

        # Baixa os anexos
        arquivos_baixados = []
        for link in links_anexos:
            nome_arquivo = os.path.join(pasta_destino, os.path.basename(link))
            with open(nome_arquivo, "wb") as arquivo_pdf:
                resposta_pdf = requests.get(link)
                resposta_pdf.raise_for_status()
                arquivo_pdf.write(resposta_pdf.content)
            arquivos_baixados.append(nome_arquivo)

        # 3. Compacta os anexos em um arquivo ZIP
        with zipfile.ZipFile(os.path.join(pasta_destino, "anexos.zip"), "w") as arquivo_zip:
            for arquivo in arquivos_baixados:
                arquivo_zip.write(arquivo, os.path.basename(arquivo))

        print(f"Anexos baixados e compactados em {os.path.join(pasta_destino, 'anexos.zip')}")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar o site ou baixar os anexos: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
    finally:
        # Limpa os arquivos PDF baixados
        if 'arquivos_baixados' in locals():
            for arquivo in arquivos_baixados:
                os.remove(arquivo)
                print(f"Arquivo {arquivo} removido.")

# URL do site com os anexos
url_ans = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

# Executa a função
baixar_e_compactar_anexos(url_ans)
