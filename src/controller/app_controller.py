from flask_jwt_extended import create_access_token

from src.utils import \
    comercializacao, \
    producao, \
    exportacao, \
    importacao, \
    processamento

from src.scrap_parameters import \
    MAX_YEAR, \
    MIN_YEAR, \
    SUB_EXPORTACAO, \
    SUB_IMPORTACAO, \
    SUB_PROCESSAMENTO

import json

class App_controller:

    def __init__(self):
        pass
        

    def signup(self, request, connection):
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        connection.create_user(email, password)


    def signin(self, request, connection):
        data        = request.get_json()
        email       = data.get('email')
        password    = data.get('password')

        if email is None or password is None:
            raise ValueError("Email and password are required!")

        user         = connection.validate_user(email, password)
        access_token = create_access_token(identity=user.email)

        return access_token


    def comercializacao(self, request):
        ano = request.args.get('ano', type=int)
        ano = ano or MAX_YEAR

        if ano < MIN_YEAR or ano > MAX_YEAR:
            raise ValueError(f'year must be in the range {MIN_YEAR} <= year <= {MAX_YEAR}')

        html = ''
        try:
            html = comercializacao.request_html(ano)
        except:
            html = comercializacao.read_html_from_cache(ano)

        data = comercializacao.scraping_html(html)
        response_data = json.dumps(data, ensure_ascii=False)
        return response_data


    def producao(self, request):
        ano = request.args.get('ano', type=int)
        ano = ano or MAX_YEAR

        if ano < MIN_YEAR or ano > MAX_YEAR:
            raise ValueError(f'year must be in the range {MIN_YEAR} <= year <= {MAX_YEAR}')

        html = ''
        try:
            html = producao.request_html(ano)
        except:
            html = producao.read_html_from_cache(ano)

        data = producao.scraping_html(html)
        response_data = json.dumps(data, ensure_ascii=False)
        return response_data


    def exportacao(self, request):
        ano         = request.args.get('ano', type=int)
        ano         = ano or 2023
        arg_subopc  = request.args.get('subopc', type=str)

        if ano < MIN_YEAR or ano > MAX_YEAR:
            raise ValueError(f'year must be in the range {MIN_YEAR} <= year <= {MAX_YEAR}')

        if not arg_subopc:
            raise ValueError(f"The argument 'subopc' is required!")

        if (arg_subopc not in SUB_EXPORTACAO.keys()):
            raise ValueError(f"The sub-option '{arg_subopc}' does not exist!")


        subopc  = SUB_EXPORTACAO[arg_subopc]
        html    = ''
        try:
            html = exportacao.request_html(ano, subopc)
        except:
            html = exportacao.read_html_from_cache(ano, arg_subopc)


        data            = exportacao.scraping_html(html)
        response_data   = json.dumps(data, ensure_ascii=False)
        
        return response_data
    

    def importacao(self, request):
        ano         = request.args.get('ano', type=int)
        ano         = ano or 2023
        arg_subopc  = request.args.get('subopc', type=str)

        if ano < MIN_YEAR or ano > MAX_YEAR:
            raise ValueError(f'year must be in the range {MIN_YEAR} <= year <= {MAX_YEAR}')

        if not arg_subopc:
            raise ValueError(f"The argument 'subopc' is required!")

        if (arg_subopc not in SUB_IMPORTACAO.keys()):
            raise ValueError(f"The sub-option '{arg_subopc}' does not exist!")


        subopc  = SUB_IMPORTACAO[arg_subopc]
        html    = ''
        try:
            html = importacao.request_html(ano, subopc)
        except:
            html = importacao.read_html_from_cache(ano, arg_subopc)


        data            = importacao.scraping_html(html)
        response_data   = json.dumps(data, ensure_ascii=False)
        
        return response_data


    def processamento(self, request):
        ano         = request.args.get('ano', type=int)
        ano         = ano or 2023
        arg_subopc  = request.args.get('subopc', type=str)

        if ano < MIN_YEAR or ano > MAX_YEAR:
            raise ValueError(f'year must be in the range {MIN_YEAR} <= year <= {MAX_YEAR}')

        if not arg_subopc:
            raise ValueError(f"The argument 'subopc' is required!")

        if (arg_subopc not in SUB_PROCESSAMENTO.keys()):
            raise ValueError(f"The sub-option '{arg_subopc}' does not exist!")


        subopc  = SUB_PROCESSAMENTO[arg_subopc]
        html    = ''
        try:
            html = processamento.request_html(ano, subopc)
        except:
            html = processamento.read_html_from_cache(ano, arg_subopc)


        data            = processamento.scraping_html(html)
        response_data   = json.dumps(data, ensure_ascii=False)
        
        return response_data















