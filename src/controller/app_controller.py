from flask_jwt_extended import \
    JWTManager, \
    create_access_token, \
    jwt_required

from src.utils import \
    comercializacao, \
    producao

from src.scrap_parameters import MAX_YEAR, MIN_YEAR

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






