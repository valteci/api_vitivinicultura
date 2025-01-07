from request_data import Request_data
import os

from scrap_parameters import \
    SAVING_PATH_PRODUCAO

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
        pass

    def update_importacao(self):
        pass

    def update_exportacao(self):
        pass

    def update_todos(self):
        pass

    def save_producao(self, html_pages: list[tuple]):
        folder = os.path.abspath('.') + SAVING_PATH_PRODUCAO
        for page in html_pages:
            file_name = f'/producao{page[1]}.html'
            saving_path = folder + file_name
            with open(saving_path, 'w') as file:
                file.write(page[0])

    def save_processamento(self, html_pages: dict):
        for subopcao in html_pages:
            folder = os.path.abspath('.') + f'/site/processamento/{subopcao}'
            os.makedirs(folder, exist_ok=True)  # Garante que o diretório existe
            for page in html_pages[subopcao]:
                file_name = f'/{subopcao}{page[1]}.html'
                saving_path = folder + file_name
                with open(saving_path, 'w') as file:
                    file.write(page[0])