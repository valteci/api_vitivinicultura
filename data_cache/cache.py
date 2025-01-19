from request_data import Request_data
import os

from environments.scrap_parameters import (
    SAVING_PATH_PRODUCAO,
    SAVING_PATH_COMERCIALIZACAO,
)

class Cache:
    """
    Classe responsável por gerenciar o cache de dados obtidos via scraping do site.

    A classe fornece métodos para realizar requisições de dados para diferentes
    categorias (produção, comercialização, exportação, importação e processamento)
    e salvar os resultados em disco. Também permite atualizar todas as categorias
    de uma só vez.
    """

    def __init__(self):
        """
        Inicializa uma instância da classe Cache.
        """
        pass


    def update_producao(self):
        """
        Atualiza os dados de produção, fazendo as requisições necessárias
        e salvando os resultados em disco.
        """
        request     = Request_data()
        html_pages  = request.request_producao()
        self.save_producao(html_pages)


    def update_processamento(self):
        """
        Atualiza os dados de processamento, processando as subopções de forma incremental.
        Salva os resultados em disco ao final de cada subopção.
        """
        request = Request_data()
        for paginas in request.request_processamento():
            self.save_processamento(paginas)


    def update_comercializacao(self):
        """
        Atualiza os dados de comercialização, fazendo as requisições necessárias
        e salvando os resultados em disco.
        """
        request     = Request_data()
        html_pages  = request.request_comercializacao()
        self.save_comercializacao(html_pages)


    def update_importacao(self):
        """
        Atualiza os dados de importação, processando as subopções de forma incremental.
        Salva os resultados em disco ao final de cada subopção.
        """
        request = Request_data()
        for paginas in request.request_importacao():
            self.save_importacao(paginas)


    def update_exportacao(self):
        """
        Atualiza os dados de exportação, processando as subopções de forma incremental.
        Salva os resultados em disco ao final de cada subopção.
        """
        request = Request_data()
        for paginas in request.request_exportacao():
            self.save_exportacao(paginas)


    def update_all(self):
        """
        Atualiza todas as categorias (produção, comercialização, exportação,
        importação e processamento).
        """
        self.update_producao()
        self.update_comercializacao()
        self.update_exportacao()
        self.update_importacao()
        self.update_processamento()


    def save_producao(self, html_pages: list[tuple]):
        """
        Salva os dados HTML de produção no disco, organizados por ano.

        Args:
            html_pages (list[tuple]): Lista de tuplas contendo o HTML da página
                e o ano correspondente.
        """
        folder = os.path.abspath('.') + SAVING_PATH_PRODUCAO
        for page in html_pages:
            file_name = f'/producao{page[1]}.html'
            saving_path = folder + file_name
            with open(saving_path, 'w') as file:
                file.write(page[0])


    def save_processamento(self, html_pages: dict):
        """
        Salva os dados HTML de processamento no disco, organizados por subopção e ano.

        Args:
            html_pages (dict): Dicionário onde a chave é a subopção e o valor
                é uma lista de tuplas contendo o HTML da página e o ano.
        """
        for subopcao in html_pages:
            folder = os.path.abspath('.') + f'data_cache/site/processamento/{subopcao}'
            os.makedirs(folder, exist_ok=True)  # Garante que o diretório existe
            for page in html_pages[subopcao]:
                file_name = f'/{subopcao}{page[1]}.html'
                saving_path = folder + file_name
                with open(saving_path, 'w') as file:
                    file.write(page[0])


    def save_comercializacao(self, html_pages: list[tuple]):
        """
        Salva os dados HTML de comercialização no disco, organizados por ano.

        Args:
            html_pages (list[tuple]): Lista de tuplas contendo o HTML da página
                e o ano correspondente.
        """
        folder = os.path.abspath('.') + SAVING_PATH_COMERCIALIZACAO
        for page in html_pages:
            file_name = f'/comercializacao{page[1]}.html'
            saving_path = folder + file_name
            with open(saving_path, 'w') as file:
                file.write(page[0])


    def save_importacao(self, html_pages: dict):
        """
        Salva os dados HTML de importação no disco, organizados por subopção e ano.

        Args:
            html_pages (dict): Dicionário onde a chave é a subopção e o valor
                é uma lista de tuplas contendo o HTML da página e o ano.
        """
        for subopcao in html_pages:
            folder = os.path.abspath('.') + f'data_cache/site/importacao/{subopcao}'
            os.makedirs(folder, exist_ok=True)  # Garante que o diretório existe
            for page in html_pages[subopcao]:
                file_name = f'/{subopcao}{page[1]}.html'
                saving_path = folder + file_name
                with open(saving_path, 'w') as file:
                    file.write(page[0])


    def save_exportacao(self, html_pages: dict):
        """
        Salva os dados HTML de exportação no disco, organizados por subopção e ano.

        Args:
            html_pages (dict): Dicionário onde a chave é a subopção e o valor
                é uma lista de tuplas contendo o HTML da página e o ano.
        """
        for subopcao in html_pages:
            folder = os.path.abspath('.') + f'data_cache/site/exportacao/{subopcao}'
            os.makedirs(folder, exist_ok=True)  # Garante que o diretório existe
            for page in html_pages[subopcao]:
                file_name = f'/{subopcao}{page[1]}.html'
                saving_path = folder + file_name
                with open(saving_path, 'w') as file:
                    file.write(page[0])


