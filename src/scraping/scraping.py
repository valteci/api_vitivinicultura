from bs4 import BeautifulSoup

class Scraping:

    def extrac_table(self, html: str) -> dict:
        """
        Extrai dados de uma tabela com a classe 'tb_base tb_dados' no HTML recebido
        e os organiza em um dicionário com as colunas como chaves.

        Args:
            html (str): HTML da página contendo a tabela.

        Returns:
            dict: Dicionário com os dados da tabela organizados por coluna.
        """
        # Parse do HTML
        scrap = BeautifulSoup(html, 'html.parser')

        # Localiza a tabela
        table = scrap.find('table', {'class': 'tb_base tb_dados'})
        if not table:
            return {}

        # Inicializa o dataset
        dataset = {}

        # Obtem os cabeçalhos (colunas) da tabela
        header_row = table.find('thead').find('tr')
        column_names = [th.text.strip() for th in header_row.find_all('th')]

        # Inicializa listas para cada coluna no dataset
        for column_name in column_names:
            dataset[column_name] = []

        # Itera sobre as linhas do corpo da tabela
        body_rows = table.find('tbody').find_all('tr')
        for row in body_rows:
            cells = row.find_all('td')
            for index, cell in enumerate(cells):
                # Adiciona o dado da célula na coluna correspondente
                column_name = column_names[index]
                dataset[column_name].append(cell.text.strip())

        return dataset