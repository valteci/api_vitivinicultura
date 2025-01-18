from src.scraping.scrap import Scraping
from src.scrap_parameters import \
    BASE_URL, \
    Opcao, \
    SAVING_PATH_COMERCIALIZACAO, \
    HEADERS

from src.scraping.scrap import Scraping
import requests



def request_html(ano: int) -> str:
    args = f'?opcao={Opcao.COMERCIALIZACAO.value}&ano={ano}'
    url = BASE_URL + args

    response = requests.get(url, headers=HEADERS, timeout=20)
    response.raise_for_status() # lança exceção se algo deu errado
    html = response.text

    return html


def read_html_from_cache(ano: int) -> str:
    path = SAVING_PATH_COMERCIALIZACAO + '/'
    file_name = f'comercializacao{ano}.html'
    html = open(path + file_name).read()

    return html


def scraping_html(html: str) -> dict:
    scrap = Scraping()
    data = scrap.extrac_table(html)
    return data
