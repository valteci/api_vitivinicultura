from src.scraping.scrap import Scraping
from src.scrap_parameters import \
    BASE_URL, \
    Opcao, \
    SAVING_PATH_EXPORTACAO, \
    HEADERS

from src.scraping.scrap import Scraping
import requests



def request_html(ano: int, subopc: str) -> str:
    url_skeleton    = BASE_URL + '?opcao={}&ano={}&subopcao={}'
    opcao           = Opcao.EXPORTACAO.value
    url             = url_skeleton.format(opcao, ano, subopc)

    response = requests.get(
        url, 
        headers=HEADERS, 
        timeout=20
    )

    response.raise_for_status()
    html = response.text
    return html


def read_html_from_cache(ano: int, subopc: str) -> str:
    path        = SAVING_PATH_EXPORTACAO + f'/{subopc}/'
    file_name   = f'{subopc}{ano}.html'
    html        = open(path + file_name).read()

    return html


def scraping_html(html: str) -> dict:
    scrap   = Scraping()
    data    = scrap.extrac_table(html)
    
    return data
