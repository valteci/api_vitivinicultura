from enum import Enum

BASE_URL = 'http://vitibrasil.cnpuv.embrapa.br/index.php'

MIN_YEAR = 1970
MAX_YEAR = 2023

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/131.0.0.0 Safari/537.36"
    )
}

class Opcao(Enum):
    PRODUCAO        = 'opt_02'
    PROCESSAMENTO   = 'opt_03'
    COMERCIALIZACAO = 'opt_04'
    IMPORTACAO      = 'opt_05'
    EXPORTACAO      = 'opt_06'


SUB_PROCESSAMENTO = {
    'viniferas'             : 'subopt_01',
    'americanas_e_hibridas' : 'subopt_02',
    'uvas_mesa'             : 'subopt_03',
    'sem_classificacao'     : 'subopt_04', 
}

SUB_IMPORTACAO = {
    'vinhos_mesa'   : 'subopt_01',
    'espumantes'    : 'subopt_02',
    'uvas_frescas'  : 'subopt_03',
    'uvas_passas'   : 'subopt_04',
    'suco_uva'      : 'subopt_05',
}

SUB_EXPORTACAO = {
    'vinhos_mesa'   : 'subopt_01',
    'espumantes'    : 'subopt_02',
    'uvas_frescas'  : 'subopt_03',
    'suco_uva'      : 'subopt_04',
}

SAVING_PATH_PRODUCAO        = 'data_cache/site/producao'
SAVING_PATH_COMERCIALIZACAO = 'data_cache/site/comercializacao'
SAVING_PATH_EXPORTACAO      = 'data_cache/site/exportacao'
SAVING_PATH_IMPORTACAO      = 'data_cache/site/importacao'
SAVING_PATH_PROCESSAMENTO   = 'data_cache/site/processamento'
