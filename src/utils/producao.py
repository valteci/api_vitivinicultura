from src.scraping.scrap import Scraping
from src.scrap_parameters import (
    BASE_URL,
    Opcao,
    SAVING_PATH_PRODUCAO,
    HEADERS,
)
import requests


def request_html(ano: int) -> str:
    """
    Faz uma requisição HTTP para obter o HTML da página de produção.

    Args:
        ano (int): O ano para o qual os dados de produção serão buscados.

    Returns:
        str: O conteúdo HTML da página de produção.

    Raises:
        requests.HTTPError: Se a requisição HTTP retornar um status de erro.
        requests.RequestException: Para outros erros relacionados à requisição.
    """
    args    = f"?opcao={Opcao.PRODUCAO.value}&ano={ano}"
    url     = BASE_URL + args

    response = requests.get(url, headers=HEADERS, timeout=20)
    response.raise_for_status()  # Lança exceção se algo deu errado
    html = response.text

    return html


def read_html_from_cache(ano: int) -> str:
    """
    Lê o HTML de produção de um arquivo cacheado.

    Args:
        ano (int): O ano para o qual os dados de produção serão buscados.

    Returns:
        str: O conteúdo HTML armazenado no arquivo cacheado.

    Raises:
        FileNotFoundError: Se o arquivo cacheado não existir.
        IOError: Se ocorrer um erro ao ler o arquivo.
    """
    path        = SAVING_PATH_PRODUCAO + "/"
    file_name   = f"producao{ano}.html"
    html        = open(path + file_name).read()

    return html


def scraping_html(html: str) -> dict:
    """
    Extrai os dados estruturados do HTML de produção.

    Args:
        html (str): O conteúdo HTML contendo os dados de produção.

    Returns:
        dict: Um dicionário contendo os dados extraídos da tabela no HTML.

    Raises:
        ValueError: Se não for possível extrair a tabela do HTML.
    """
    scrap   = Scraping()
    data    = scrap.extrac_table(html)
    
    return data
