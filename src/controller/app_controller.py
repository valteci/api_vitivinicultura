from flask_jwt_extended import create_access_token

from src.utils import (
    comercializacao,
    producao,
    exportacao,
    importacao,
    processamento,
)

from src.scrap_parameters import (
    MAX_YEAR,
    MIN_YEAR,
    SUB_EXPORTACAO,
    SUB_IMPORTACAO,
    SUB_PROCESSAMENTO,
)

import json


class App_controller:
    """
    Controlador principal da API.

    Este controlador gerencia as operações principais da API, incluindo autenticação
    de usuários e processamento de dados relacionados a comercialização, produção,
    exportação, importação e processamento. Ele atua como intermediário entre as
    rotas Flask e os utilitários de scraping e banco de dados.
    """

    def __init__(self):
        """
        Inicializa a instância do controlador.
        """
        pass

    def signup(self, request, connection):
        """
        Processa o cadastro de um novo usuário.

        Args:
            request: O objeto de requisição contendo os dados do usuário.
            connection: A conexão com o banco de dados.

        Raises:
            ValueError: Se os dados do usuário não forem válidos.
        """
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")
        connection.create_user(email, password)


    def signin(self, request, connection):
        """
        Processa a autenticação de um usuário e gera um token de acesso.

        Args:
            request: O objeto de requisição contendo os dados do usuário.
            connection: A conexão com o banco de dados.

        Returns:
            str: O token de acesso gerado para o usuário.

        Raises:
            ValueError: Se os dados do usuário forem inválidos.
        """
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")

        if email is None or password is None:
            raise ValueError("Email and password are required!")

        user = connection.validate_user(email, password)
        access_token = create_access_token(identity=user.email)

        return access_token


    def comercializacao(self, request):
        """
        Processa dados relacionados à comercialização.

        Args:
            request: O objeto de requisição contendo os parâmetros de ano.

        Returns:
            str: Dados de comercialização em formato JSON.

        Raises:
            ValueError: Se os parâmetros forem inválidos.
        """
        ano = request.args.get("ano", type=int) or MAX_YEAR

        if ano < MIN_YEAR or ano > MAX_YEAR:
            raise ValueError(f"year must be in the range {MIN_YEAR} <= year <= {MAX_YEAR}")

        try:
            html = comercializacao.request_html(ano)
        except:
            html = comercializacao.read_html_from_cache(ano)

        data = comercializacao.scraping_html(html)
        return json.dumps(data, ensure_ascii=False)


    def producao(self, request):
        """
        Processa dados relacionados à produção.

        Args:
            request: O objeto de requisição contendo os parâmetros de ano.

        Returns:
            str: Dados de produção em formato JSON.

        Raises:
            ValueError: Se os parâmetros forem inválidos.
        """
        ano = request.args.get("ano", type=int) or MAX_YEAR

        if ano < MIN_YEAR or ano > MAX_YEAR:
            raise ValueError(f"year must be in the range {MIN_YEAR} <= year <= {MAX_YEAR}")

        try:
            html = producao.request_html(ano)
        except:
            html = producao.read_html_from_cache(ano)

        data = producao.scraping_html(html)
        return json.dumps(data, ensure_ascii=False)


    def exportacao(self, request):
        """
        Processa dados relacionados à exportação.

        Args:
            request: O objeto de requisição contendo os parâmetros de ano e subopção.

        Returns:
            str: Dados de exportação em formato JSON.

        Raises:
            ValueError: Se os parâmetros forem inválidos ou ausentes.
        """
        ano = request.args.get("ano", type=int) or MAX_YEAR
        arg_subopc = request.args.get("subopc", type=str)

        if ano < MIN_YEAR or ano > MAX_YEAR:
            raise ValueError(f"year must be in the range {MIN_YEAR} <= year <= {MAX_YEAR}")

        if not arg_subopc:
            raise ValueError("The argument 'subopc' is required!")

        if arg_subopc not in SUB_EXPORTACAO.keys():
            raise ValueError(f"The sub-option '{arg_subopc}' does not exist!")

        subopc = SUB_EXPORTACAO[arg_subopc]

        try:
            html = exportacao.request_html(ano, subopc)
        except:
            html = exportacao.read_html_from_cache(ano, arg_subopc)

        data = exportacao.scraping_html(html)
        return json.dumps(data, ensure_ascii=False)


    def importacao(self, request):
        """
        Processa dados relacionados à importação.

        Args:
            request: O objeto de requisição contendo os parâmetros de ano e subopção.

        Returns:
            str: Dados de importação em formato JSON.

        Raises:
            ValueError: Se os parâmetros forem inválidos ou ausentes.
        """
        ano = request.args.get("ano", type=int) or MAX_YEAR
        arg_subopc = request.args.get("subopc", type=str)

        if ano < MIN_YEAR or ano > MAX_YEAR:
            raise ValueError(f"year must be in the range {MIN_YEAR} <= year <= {MAX_YEAR}")

        if not arg_subopc:
            raise ValueError("The argument 'subopc' is required!")

        if arg_subopc not in SUB_IMPORTACAO.keys():
            raise ValueError(f"The sub-option '{arg_subopc}' does not exist!")

        subopc = SUB_IMPORTACAO[arg_subopc]

        try:
            html = importacao.request_html(ano, subopc)
        except:
            html = importacao.read_html_from_cache(ano, arg_subopc)

        data = importacao.scraping_html(html)
        return json.dumps(data, ensure_ascii=False)


    def processamento(self, request):
        """
        Processa dados relacionados ao processamento.

        Args:
            request: O objeto de requisição contendo os parâmetros de ano e subopção.

        Returns:
            str: Dados de processamento em formato JSON.

        Raises:
            ValueError: Se os parâmetros forem inválidos ou ausentes.
        """
        ano = request.args.get("ano", type=int) or MAX_YEAR
        arg_subopc = request.args.get("subopc", type=str)

        if ano < MIN_YEAR or ano > MAX_YEAR:
            raise ValueError(f"year must be in the range {MIN_YEAR} <= year <= {MAX_YEAR}")

        if not arg_subopc:
            raise ValueError("The argument 'subopc' is required!")

        if arg_subopc not in SUB_PROCESSAMENTO.keys():
            raise ValueError(f"The sub-option '{arg_subopc}' does not exist!")

        subopc = SUB_PROCESSAMENTO[arg_subopc]

        try:
            html = processamento.request_html(ano, subopc)
        except:
            html = processamento.read_html_from_cache(ano, arg_subopc)

        data = processamento.scraping_html(html)
        return json.dumps(data, ensure_ascii=False)

