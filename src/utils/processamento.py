from src.scraping.scrap import Scraping
from environments.scrap_parameters import (
    BASE_URL,
    Opcao,
    SAVING_PATH_PROCESSAMENTO,
    HEADERS,
)
import requests


def request_html(ano: int, subopc: str) -> str:
    """
    Faz uma requisição HTTP para obter o HTML da página de processamento.

    Args:
        ano (int): O ano para o qual os dados de processamento serão buscados.
        subopc (str): A subopção específica para o tipo de dado de processamento.

    Returns:
        str: O conteúdo HTML da página de processamento.

    Raises:
        requests.HTTPError: Se a requisição HTTP retornar um status de erro.
        requests.RequestException: Para outros erros relacionados à requisição.
    """
    url_skeleton    = BASE_URL + "?opcao={}&ano={}&subopcao={}"
    opcao           = Opcao.PROCESSAMENTO.value
    url             = url_skeleton.format(opcao, ano, subopc)

    response = requests.get(
        url,
        headers=HEADERS,
        timeout=20,
    )

    response.raise_for_status()  # Lança exceção se algo deu errado
    html = response.text
    return html


def read_html_from_cache(ano: int, subopc: str) -> str:
    """
    Lê o HTML de processamento de um arquivo cacheado.

    Args:
        ano (int): O ano para o qual os dados de processamento serão buscados.
        subopc (str): A subopção específica para o tipo de dado de processamento.

    Returns:
        str: O conteúdo HTML armazenado no arquivo cacheado.

    Raises:
        FileNotFoundError: Se o arquivo cacheado não existir.
        IOError: Se ocorrer um erro ao ler o arquivo.
    """
    path        = SAVING_PATH_PROCESSAMENTO + f"/{subopc}/"
    file_name   = f"{subopc}{ano}.html"
    html        = open(path + file_name).read()

    return html


def scraping_html(html: str) -> dict:
    """
    Extrai os dados estruturados do HTML de processamento.

    Args:
        html (str): O conteúdo HTML contendo os dados de processamento.

    Returns:
        dict: Um dicionário contendo os dados extraídos da tabela no HTML.

    Raises:
        ValueError: Se não for possível extrair a tabela do HTML.
    """
    scrap   = Scraping()
    data    = scrap.extrac_table(html)
    
    return data
