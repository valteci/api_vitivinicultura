import requests
from requests.exceptions import RequestException
from time import sleep
from random import randint

from environments.scrap_parameters import (
    Opcao,
    SUB_PROCESSAMENTO,
    SUB_IMPORTACAO,
    SUB_EXPORTACAO,
    BASE_URL,
    MAX_YEAR,
    MIN_YEAR,
    HEADERS
)


class Request_data:
    """
    Classe responsável por gerenciar as requisições de páginas HTML do site.

    Essa classe implementa métodos para baixar dados de várias categorias (produção,
    processamento, comercialização, importação e exportação). Inclui um sistema
    robusto de requisições, com tentativas repetidas em caso de falhas e
    espera aleatória entre as requisições para evitar sobrecarregar o site.

    """


    def __init__(self):
        """
        Inicializa uma instância da classe Request_data.
        """
        pass


    def request_producao(self) -> list[tuple]:
        """
        Realiza requisições para obter dados de produção.

        Returns:
            list[tuple]: Lista de tuplas contendo o HTML da página e o ano correspondente.
        """
        html_pages = []

        for ano in range(MIN_YEAR, MAX_YEAR + 1):
            url = BASE_URL + f"?ano={ano}&opcao={Opcao.PRODUCAO.value}"
            success = False
            attempt = 0

            while not success:
                try:
                    attempt += 1
                    print(f"Tentativa {attempt} para o ano {ano}...")
                    self.wait()
                    response = requests.get(url, headers=HEADERS, timeout=20)
                    response.raise_for_status()
                    html_pages.append((response.text, ano))
                    print(f"Requisição para o ano {ano} bem-sucedida.")
                    success = True
                except requests.RequestException as e:
                    print(f"Erro na tentativa {attempt} para o ano {ano}: {e}")
                    print("Tentando novamente...")

        return html_pages


    def request_processamento(self):
        """
        Realiza requisições para obter dados de processamento.

        Yields:
            dict: Um dicionário onde a chave é a subopção e o valor é uma lista de
            tuplas contendo o HTML da página e o ano correspondente.
        """
        url_parte_fixa = f"{BASE_URL}?opcao={Opcao.PROCESSAMENTO.value}"
        for subopc in SUB_PROCESSAMENTO:
            html_pages = []
            url_opcao = f"{url_parte_fixa}&subopcao={SUB_PROCESSAMENTO[subopc]}"

            for ano in range(MIN_YEAR, MAX_YEAR + 1):
                url = f"{url_opcao}&ano={ano}"
                success = False
                attempt = 0

                while not success:
                    try:
                        attempt += 1
                        print(f"Tentativa {attempt} para o ano {ano}, subopção {subopc}...")
                        self.wait()
                        response = requests.get(url, headers=HEADERS, timeout=20)
                        response.raise_for_status()
                        html_pages.append((response.text, ano))
                        print(f"Requisição para o ano {ano}, subopção {subopc} bem-sucedida.")
                        success = True
                    except requests.RequestException as e:
                        print(f"Erro na tentativa {attempt} para o ano {ano}, subopção {subopc}: {e}")
                        print("Tentando novamente...")

            yield {subopc: html_pages}


    def request_comercializacao(self) -> list[tuple]:
        """
        Realiza requisições para obter dados de comercialização.

        Returns:
            list[tuple]: Lista de tuplas contendo o HTML da página e o ano correspondente.
        """
        html_pages = []

        for ano in range(MIN_YEAR, MAX_YEAR + 1):
            url = BASE_URL + f"?ano={ano}&opcao={Opcao.COMERCIALIZACAO.value}"
            success = False
            attempt = 0

            while not success:
                try:
                    attempt += 1
                    print(f"Tentativa {attempt} para o ano {ano}...")
                    self.wait()
                    response = requests.get(url, headers=HEADERS, timeout=20)
                    response.raise_for_status()
                    html_pages.append((response.text, ano))
                    print(f"Requisição para o ano {ano} bem-sucedida.")
                    success = True
                except requests.RequestException as e:
                    print(f"Erro na tentativa {attempt} para o ano {ano}: {e}")
                    print("Tentando novamente...")

        return html_pages


    def request_importacao(self):
        """
        Realiza requisições para obter dados de importação.

        Yields:
            dict: Um dicionário onde a chave é a subopção e o valor é uma lista de
            tuplas contendo o HTML da página e o ano correspondente.
        """
        url_parte_fixa = f"{BASE_URL}?opcao={Opcao.IMPORTACAO.value}"
        for subopc in SUB_IMPORTACAO:
            html_pages = []
            url_opcao = f"{url_parte_fixa}&subopcao={SUB_IMPORTACAO[subopc]}"

            for ano in range(MIN_YEAR, MAX_YEAR + 1):
                url = f"{url_opcao}&ano={ano}"
                success = False
                attempt = 0

                while not success:
                    try:
                        attempt += 1
                        print(f"Tentativa {attempt} para o ano {ano}, subopção {subopc}...")
                        self.wait()
                        response = requests.get(url, headers=HEADERS, timeout=20)
                        response.raise_for_status()
                        html_pages.append((response.text, ano))
                        print(f"Requisição para o ano {ano}, subopção {subopc} bem-sucedida.")
                        success = True
                    except requests.RequestException as e:
                        print(f"Erro na tentativa {attempt} para o ano {ano}, subopção {subopc}: {e}")
                        print("Tentando novamente...")

            yield {subopc: html_pages}


    def request_exportacao(self):
        """
        Realiza requisições para obter dados de exportação.

        Yields:
            dict: Um dicionário onde a chave é a subopção e o valor é uma lista de
            tuplas contendo o HTML da página e o ano correspondente.
        """
        url_parte_fixa = f"{BASE_URL}?opcao={Opcao.EXPORTACAO.value}"
        for subopc in SUB_EXPORTACAO:
            html_pages = []
            url_opcao = f"{url_parte_fixa}&subopcao={SUB_EXPORTACAO[subopc]}"

            for ano in range(MIN_YEAR, MAX_YEAR + 1):
                url = f"{url_opcao}&ano={ano}"
                success = False
                attempt = 0

                while not success:
                    try:
                        attempt += 1
                        print(f"Tentativa {attempt} para o ano {ano}, subopção {subopc}...")
                        self.wait()
                        response = requests.get(url, headers=HEADERS, timeout=20)
                        response.raise_for_status()
                        html_pages.append((response.text, ano))
                        print(f"Requisição para o ano {ano}, subopção {subopc} bem-sucedida.")
                        success = True
                    except requests.RequestException as e:
                        print(f"Erro na tentativa {attempt} para o ano {ano}, subopção {subopc}: {e}")
                        print("Tentando novamente...")

            yield {subopc: html_pages}


    def wait(self):
        """
        Aguarda um tempo aleatório entre as requisições.

        O tempo de espera varia entre 10 e 15 segundos.
        """
        MIN_TIME = 10
        MAX_TIME = 15
        wait_time = randint(MIN_TIME, MAX_TIME)
        sleep(wait_time)
