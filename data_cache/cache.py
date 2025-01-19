from request_data import Request_data
import os

from environments.scrap_parameters import \
    SAVING_PATH_PRODUCAO, \
    SAVING_PATH_COMERCIALIZACAO

class Cache:
    def __init__(self):
        pass

    def update_producao(self):
        request = Request_data()
        html_pages = request.request_producao()
        self.save_producao(html_pages)

    def update_processamento(self):
        request = Request_data()
        for paginas in request.request_processamento():
            self.save_processamento(paginas)

    def update_comercializacao(self):
        request = Request_data()
        html_pages = request.request_comercializacao()
        self.save_comercializacao(html_pages)

    def update_importacao(self):
        request = Request_data()
        for paginas in request.request_importacao():
            self.save_importacao(paginas)

    def update_exportacao(self):
        request = Request_data()
        for paginas in request.request_exportacao():
            self.save_exportacao(paginas)

    def update_todos(self):
        self.update_producao()
        self.update_comercializacao()
        self.update_exportacao()
        self.update_importacao()
        self.update_processamento()

    def save_producao(self, html_pages: list[tuple]):
        folder = os.path.abspath('.') + SAVING_PATH_PRODUCAO
        for page in html_pages:
            file_name = f'/producao{page[1]}.html'
            saving_path = folder + file_name
            with open(saving_path, 'w') as file:
                file.write(page[0])

    def save_processamento(self, html_pages: dict):
        for subopcao in html_pages:
            folder = os.path.abspath('.') + f'data_cache/site/processamento/{subopcao}'
            os.makedirs(folder, exist_ok=True)  # Garante que o diretório existe
            for page in html_pages[subopcao]:
                file_name = f'/{subopcao}{page[1]}.html'
                saving_path = folder + file_name
                with open(saving_path, 'w') as file:
                    file.write(page[0])

    def save_comercializacao(self, html_pages: list[tuple]):
        folder = os.path.abspath('.') + SAVING_PATH_COMERCIALIZACAO
        for page in html_pages:
            file_name = f'/comercializacao{page[1]}.html'
            saving_path = folder + file_name
            with open(saving_path, 'w') as file:
                file.write(page[0])

    def save_importacao(self, html_pages: dict):
        for subopcao in html_pages:
            folder = os.path.abspath('.') + f'data_cache/site/importacao/{subopcao}'
            os.makedirs(folder, exist_ok=True)  # Garante que o diretório existe
            for page in html_pages[subopcao]:
                file_name = f'/{subopcao}{page[1]}.html'
                saving_path = folder + file_name
                with open(saving_path, 'w') as file:
                    file.write(page[0])


    def save_exportacao(self, html_pages: dict):
        for subopcao in html_pages:
            folder = os.path.abspath('.') + f'data_cache/site/exportacao/{subopcao}'
            os.makedirs(folder, exist_ok=True)  # Garante que o diretório existe
            for page in html_pages[subopcao]:
                file_name = f'/{subopcao}{page[1]}.html'
                saving_path = folder + file_name
                with open(saving_path, 'w') as file:
                    file.write(page[0])



