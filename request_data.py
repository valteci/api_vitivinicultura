import requests
from requests.exceptions import RequestException
from time import sleep
from random import randint

from scrap_parameters import \
    Opcao, \
    SUB_PROCESSAMENTO, \
    SUB_IMPORTACAO, \
    SUB_EXPORTACAO, \
    BASE_URL, \
    MAX_YEAR, \
    MIN_YEAR

class Request_data:
    def __init__(self):
        pass

    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    }

    def request_producao(self) -> list[tuple]:
        html_pages = []
    
        for ano in range(MIN_YEAR, MAX_YEAR + 1):
            url = BASE_URL + '?ano=' + str(ano) + '&opcao=' + Opcao.PRODUCAO.value
            success = False  # Flag para indicar sucesso
            attempt = 0      # Contador de tentativas
            
            while not success:  # Tentativas indefinidas até obter sucesso
                try:
                    attempt += 1
                    print(f"Tentativa {attempt} para o ano {ano}...")
                    self.wait()  # Espera de 10 a 15 segundos
                    response = requests.get(url, headers=self.HEADERS, timeout=20)
                    response.raise_for_status()  # Lança exceção para códigos de erro HTTP
                    html_content = response.text
                    page = (html_content, ano)
                    html_pages.append(page)
                    print(f"Requisição para o ano {ano} bem-sucedida na tentativa {attempt}.")
                    success = True  # Requisição bem-sucedida, sai do loop
                except requests.HTTPError as http_err:
                    print(f"Erro HTTP para o ano {ano}: {http_err}")
                except requests.Timeout:
                    print(f"Erro de timeout na tentativa {attempt} para o ano {ano}.")
                except RequestException as req_err:
                    print(f"Erro geral na tentativa {attempt} para o ano {ano}: {req_err}")
                finally:
                    if not success:
                        print("Tentando novamente...")

        return html_pages


    def request_processamento(self):
        html_pages = {}
        url_parte_fixa = f'{BASE_URL}?opcao={Opcao.PROCESSAMENTO.value}'
        for subopc in SUB_PROCESSAMENTO:
            url_opcao = f'{url_parte_fixa}&subopcao={SUB_PROCESSAMENTO[subopc]}'
            html_pages[subopc] = []
            for ano in range(MIN_YEAR, MAX_YEAR + 1):
                url = f'{url_opcao}&ano={ano}'
                success = False  # Flag para indicar sucesso
                attempt = 0      # Contador de tentativas
                
                while not success:
                    try:
                        attempt += 1
                        print(f"Tentativa {attempt} para o ano {ano}...")
                        self.wait()  # Espera de 10 a 15 segundos
                        response = requests.get(url, headers=self.HEADERS, timeout=20)
                        response.raise_for_status()  # Lança exceção para códigos de erro HTTP
                        html_content = response.text
                        page = (html_content, ano)
                        html_pages[subopc].append(page)
                        print(f"Requisição para o ano {ano} bem-sucedida na tentativa {attempt}.")
                        success = True  # Requisição bem-sucedida, sai do loop
                    except requests.HTTPError as http_err:
                        print(f"Erro HTTP para o ano {ano}: {http_err}")
                    except requests.Timeout:
                        print(f"Erro de timeout na tentativa {attempt} para o ano {ano}.")
                    except RequestException as req_err:
                        print(f"Erro geral na tentativa {attempt} para o ano {ano}: {req_err}")
                    finally:
                        if not success:
                            print("Tentando novamente...")
                
            yield ({subopc: html_pages[subopc]})


    def request_comercializacao(self) -> list[tuple]:
        html_pages = []
    
        for ano in range(MIN_YEAR, MAX_YEAR + 1):
            url = BASE_URL + '?ano=' + str(ano) + '&opcao=' + Opcao.COMERCIALIZACAO.value
            success = False  # Flag para indicar sucesso
            attempt = 0      # Contador de tentativas
            
            while not success:  # Tentativas indefinidas até obter sucesso
                try:
                    attempt += 1
                    print(f"Tentativa {attempt} para o ano {ano}...")
                    self.wait()  # Espera de 10 a 15 segundos
                    response = requests.get(url, headers=self.HEADERS, timeout=20)
                    response.raise_for_status()  # Lança exceção para códigos de erro HTTP
                    html_content = response.text
                    page = (html_content, ano)
                    html_pages.append(page)
                    print(f"Requisição para o ano {ano} bem-sucedida na tentativa {attempt}.")
                    success = True  # Requisição bem-sucedida, sai do loop
                except requests.HTTPError as http_err:
                    print(f"Erro HTTP para o ano {ano}: {http_err}")
                except requests.Timeout:
                    print(f"Erro de timeout na tentativa {attempt} para o ano {ano}.")
                except RequestException as req_err:
                    print(f"Erro geral na tentativa {attempt} para o ano {ano}: {req_err}")
                finally:
                    if not success:
                        print("Tentando novamente...")

        return html_pages


    def request_importacao(self):
        html_pages = {}
        url_parte_fixa = f'{BASE_URL}?opcao={Opcao.IMPORTACAO.value}'
        for subopc in SUB_IMPORTACAO:
            url_opcao = f'{url_parte_fixa}&subopcao={SUB_IMPORTACAO[subopc]}'
            html_pages[subopc] = []
            for ano in range(MIN_YEAR, MAX_YEAR + 1):
                url = f'{url_opcao}&ano={ano}'
                success = False  # Flag para indicar sucesso
                attempt = 0      # Contador de tentativas
                
                while not success:
                    try:
                        attempt += 1
                        print(f"Tentativa {attempt} para o ano {ano}...")
                        self.wait()  # Espera de 10 a 15 segundos
                        response = requests.get(url, headers=self.HEADERS, timeout=20)
                        response.raise_for_status()  # Lança exceção para códigos de erro HTTP
                        html_content = response.text
                        page = (html_content, ano)
                        html_pages[subopc].append(page)
                        print(f"Requisição para o ano {ano} bem-sucedida na tentativa {attempt}.")
                        success = True  # Requisição bem-sucedida, sai do loop
                    except requests.HTTPError as http_err:
                        print(f"Erro HTTP para o ano {ano}: {http_err}")
                    except requests.Timeout:
                        print(f"Erro de timeout na tentativa {attempt} para o ano {ano}.")
                    except RequestException as req_err:
                        print(f"Erro geral na tentativa {attempt} para o ano {ano}: {req_err}")
                    finally:
                        if not success:
                            print("Tentando novamente...")
                
            yield ({subopc: html_pages[subopc]})



    def wait(self):
        MIN_TIME = 10
        MAX_TIME = 15
        wait_time = randint(MIN_TIME, MAX_TIME)
        sleep(wait_time)