## INTRODUÇÃO

Esta API foi desenvolvida como parte do Tech Challenge da pós-graduação em Machine Learning Engineering. Ela realiza web scraping no site da Embrapa para coletar dados sobre vitivinicultura nas seguintes categorias:
- Produção
- Processamento
- Comercialização
- Importação
- Exportação

O objetivo principal é fornecer uma API pública para consulta desses dados, que podem futuramente ser utilizados em modelos de Machine Learning. A API foi implantada no [render](https://render.com) e está disponível no seguinte link: [url] 

## COMO RODAR LOCALMENTE

Para executar a API localmente, siga os passos abaixo, você pode rodar com um "virtual environment" (venv) ou no docker:

### RODANDO NO DOCKER

1. Clone o repositório e entre no mesmo:
   ```bash
   git clone https://github.com/valteci/api_vitivinicultura
   cd api_vitivinicultura
   ```

2. Construa uma imagem do dockerfile:
    ```bash
    docker build -t api .
    ```

3. Crie um contêiner a partir da imagem passando a variável de ambiente "JWT_SECRET_KEY", que será usada para gerar os tokens de acesso, o valor abaixo é um exemplo:
    ```bash
    docker run -e JWT_SECRET_KEY="SDJF39SNSDL24V" -dp 5000:5000 api
    ```

Você pode mudar o valor da variável de ambiente FLASK_ENV dentro do dockerfile para "production" caso queira rodar o contêiner em modo de produção

### RODANDO COM UM AMBIENTE VIRTUAL PYTHON (VENV)

1. Clone o repositório e entre no mesmo:
   ```bash
   git clone https://github.com/valteci/api_vitivinicultura
   cd api_vitivinicultura
   ```

2. Crie um ambiente virtual Python (recomendado):
   ```bash
   python3 -m venv .venv
   ```

3. Ative o ambiente virtual

   se estiver no Linux ou MacOS, use esse comando:
   ```bash
   source .venv/bin/activate
   ```

   Caso esteja no Windows, use esse comando:
   ```bash
   .\.venv\Scripts\activate
   ```

   Se o windows te proibir de executar o script devido a política de execução de script, abra o powershell como administrador e rode oseguinte comando e aperte "Y" e enter:
   ```bash
   Set-ExecutionPolicy RemoteSigned -Scope CurrentUse
   ```

4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Defina a variável de ambiente JWT_SECRET_KEY, [essa variável define o "secret" para o jwt](https://stackoverflow.com/questions/31309759/what-is-secret-key-for-jwt-based-authentication-and-how-to-generate-it):

   No Linux ou MacOs defina um valor para JWT_SECRET_KEY com o seguinte comando:  
   ```bash
   export JWT_SECRET_KEY="SEU_VALOR_AQUI"
   ```

   No Windows, execute o seguinte comando no powershell:
   ```bash
   $env:JWT_SECRET_KEY="SEU_VALOR_AQUI"
   ```

5. Execute a API:

   Para executar a API em modo de desenvolvimento no Linux, macOs e no Windows:
   ```bash
   flask run 
   ```

   Para executar a API em modo de produção no Linux:
   ```bash
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```

   Para executar a API em modo de produção no Windows:
   ```bash
    waitress-serve --port=5000 app:app
   ```


A API estará acessível em `http://127.0.0.1:5000` ou em `http://localhost:5000`.

Para desativar o ambiente virtual python (venv):
   ```bash
   deactivate
   ```

## AUTENTICAÇÃO DA API

Esta API utiliza autenticação baseada em tokens JWT (JSON Web Tokens) para garantir que apenas usuários autorizados tenham acesso a determinadas rotas. Para autenticar:

1. Obtenha um token JWT enviando uma requisição POST para a rota `/auth` com suas credenciais.

2. Inclua o token JWT no cabeçalho de autorização ao fazer chamadas para rotas protegidas:
   ```
   Authorization: Bearer <seu_token>
   ```

Certifique-se de manter seu token seguro.

## ROTAS E PARÂMETROS DA API

Aqui estão as principais rotas disponíveis na API:

1. **GET `/producao`**
   - Descrição: Retorna dados de produção.
   - Parâmetros opcionais:
     - `ano`: Filtra os dados pelo ano (e.g., `2023`).

2. **GET `/processamento`**
   - Descrição: Retorna dados de processamento.
   - Parâmetros opcionais:
     - `tipo`: Filtra pelo tipo de processamento.

3. **GET `/comercializacao`**
   - Descrição: Retorna dados de comercialização.
   - Parâmetros opcionais:
     - `regiao`: Filtra pela região (e.g., `Sul`, `Sudeste`).

4. **GET `/importacao`**
   - Descrição: Retorna dados de importação.
   - Parâmetros opcionais:
     - `pais_origem`: Filtra pelo país de origem.

5. **GET `/exportacao`**
   - Descrição: Retorna dados de exportação.
   - Parâmetros opcionais:
     - `destino`: Filtra pelo país de destino.

Inclua nos cabeçalhos das chamadas qualquer parâmetro de autenticação necessário.

