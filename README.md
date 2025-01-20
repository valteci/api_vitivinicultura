## INTRODUÇÃO

Esta API foi desenvolvida como parte do Tech Challenge da pós-graduação em Machine Learning Engineering. Ela realiza web scraping no [site da Embrapa](http://vitibrasil.cnpuv.embrapa.br/index.php) para coletar dados sobre vitivinicultura nas seguintes categorias:
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

Você pode mudar o valor da variável de ambiente FLASK_ENV dentro do dockerfile para "production" caso queira rodar o contêiner em modo de produção, o que é útil para implantar em servidores reais, pois otimiza o desempenho da API.

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

   se estiver no Linux ou macOS, use esse comando:
   ```bash
   source .venv/bin/activate
   ```

   Caso esteja no Windows, use esse comando:
   ```bash
   .\.venv\Scripts\activate
   ```

   Se o Windows te proibir de executar o script devido a política de execução de scripts, abra o powershell como administrador e rode o seguinte comando e aperte "Y" e enter:
   ```bash
   Set-ExecutionPolicy RemoteSigned -Scope CurrentUse
   ```

4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Defina a variável de ambiente JWT_SECRET_KEY, [essa variável define o "secret" para o jwt](https://stackoverflow.com/questions/31309759/what-is-secret-key-for-jwt-based-authentication-and-how-to-generate-it):

   No Linux ou macOS defina um valor para JWT_SECRET_KEY com o seguinte comando:  
   ```bash
   export JWT_SECRET_KEY="SEU_VALOR_AQUI"
   ```

   No Windows, execute o seguinte comando no powershell:
   ```bash
   $env:JWT_SECRET_KEY="SEU_VALOR_AQUI"
   ```

5. Execute a API:

   Para executar a API em modo de desenvolvimento no Linux, macOS e no Windows:
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
   OBS: O modo de produção é útil se você for rodar o projeto em um servidor real, pois otimiza o desempenho da API.



Depois disso, a API estará acessível em `http://127.0.0.1:5000` ou em `http://localhost:5000`.

Para desativar o ambiente virtual python (venv):
   ```bash
   deactivate
   ```

## AUTENTICAÇÃO DA API

Esta API utiliza autenticação baseada em tokens JWT (JSON Web Tokens) para garantir que apenas usuários autorizados tenham acesso a determinadas rotas. É importante que você escolha um bom valor para a variável de ambiente [JWT_SECRET_KEY](https://stackoverflow.com/questions/31309759/what-is-secret-key-for-jwt-based-authentication-and-how-to-generate-it) e que mantenha ela segura. Para autenticar:

1. Faça seu cadastro na API através de uma requisição POST para a rota `/signup` enviando um JSON no corpo da requisição que contenha os campos `email` e `password`. Veja um exemplo de JSON:
   ```json
   {
	   "email": "usuario@gmail.com",
	   "password": "12345678"
   }
   ```

2. Depois de se cadastrar, faça login na API para receber seu token de acesso. Para isso, envie uma requisição POST para a rota `/signin` com um JSON no corpo da requisição que contenha os campos `email` e `password`. O estilo do JSON é o mesmo que o do exemplo acima. A resposta dessa rota é um JSON contendo o seu token de acesso, copie esse token e guarde-o, pois você precisará dele para fazer requisições para todas as outras rotas da API. Exemplo de resposta da rota `/signin`:
   ```json
   {
	"access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTczNzMxNTc4MywianRpIjoiYjA0MTY2ZWUtZTgxOS00NDcwLWE4ZDMtOTliMjlkMzRjNjFjIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Impvc2VAZ21haWwuY29tIiwibmJmIjoxNzM3MzE1NzgzLCJjc3JmIjoiMTg3NGVhMDAtOWJmMC00ZTNkLWE5MzItODM3Njc3MzA3NTg5IiwiZXhwIjoxNzM3MzE3NTgzfQ.SURBeoHJeGWDc1VMwjBrW3qye9B72Z1tcRqKT60tbPA"
   }
   ```

3. Com o access token em mãos, você pode fazer requisições para todas as outras rotas da API. Nesse caso, você vai precisar passar esse token em cada requisição. Para fazer isso, adicione o cabeçalho `Authorization` na sua requisição, o valor desse cabeçalho vai ser `Bearer <seu_access_token>`, ou seja, a palavra Bearer seguindo pelo seu access token que recebeu ao fazer o login. O access token tem duração de 30 minutos, quando ele expirar, você vai precisar fazer login novamente, obtendo um novo token.


## ROTAS E PARÂMETROS DA API

Aqui estão as rotas disponíveis na API, bem como os seus parâmetros:

1. **GET `/producao`**
   - Descrição: Retorna dados de produção.

   - Parâmetros:
     - `ano`: Filtra os dados pelo ano, que deve ser um valor entre 1970 a 2023. Caso esse parâmetro seja omitido, será considerado o ano de 2023.

   - Retorno: JSON contendo os dados da tabela.

   - Exemplo de uso:
      ```bash
      curl "http://localhost:5000/producao?ano=1970" -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTczNzMzMjkzMCwianRpIjoiMzBmODgxNDItMDgyZS00ZDFkLTkxMTAtNGI1N2IyYjU3ZmE5IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InVzZXJAZ21haWwuY29tIiwibmJmIjoxNzM3MzMyOTMwLCJjc3JmIjoiNzRjN2YzMDctZjAxMy00NDBhLTk4MmQtOWJhNTZiNmY3MzAzIiwiZXhwIjoxNzM3MzM0NzMwfQ.oDcrt_VcY4I4sq1FnUZeNIOeFaBGn2e7_sfG5YyL9b8"
      ```


2. **GET `/processamento`**
   - Descrição: Retorna dados de processamento que podem ser classificados em: `viníferas`, `americanas e híbridas`, `uvas de mesa` e `sem classificação`

   - Parâmetros:
     - `ano`: Filtra os dados pelo ano, que deve ser um valor entre 1970 a 2023. Caso esse parâmetro seja omitido, será considerado o ano de 2023.

     - `subopc`: Seleciona uma das opções. Esse parâmetro pode ter os seguintes valores: `viniferas`, `americanas_e_hibridas`, `uvas_mesa` e `sem_classificacao`.

   - Retorno: JSON contendo os dados da tabela.

   - Exemplo de uso:
      ```bash
       curl "http://localhost:5000/processamento?ano=2023&subopc=viniferas" -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTczNzMzMjkzMCwianRpIjoiMzBmODgxNDItMDgyZS00ZDFkLTkxMTAtNGI1N2IyYjU3ZmE5IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InVzZXJAZ21haWwuY29tIiwibmJmIjoxNzM3MzMyOTMwLCJjc3JmIjoiNzRjN2YzMDctZjAxMy00NDBhLTk4MmQtOWJhNTZiNmY3MzAzIiwiZXhwIjoxNzM3MzM0NzMwfQ.oDcrt_VcY4I4sq1FnUZeNIOeFaBGn2e7_sfG5YyL9b8"
      ```


3. **GET `/comercializacao`**
   - Descrição: Retorna dados de comercialização.

   - Parâmetros:
     - `ano`: Filtra os dados pelo ano, que deve ser um valor entre 1970 a 2023. Caso esse parâmetro seja omitido, será considerado o ano de 2023.

   - Retorno: JSON contendo os dados da tabela.

   - Exemplo de uso:
      ```bash
      curl "http://localhost:5000/comercializacao?ano=1977" -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTczNzMzMjkzMCwianRpIjoiMzBmODgxNDItMDgyZS00ZDFkLTkxMTAtNGI1N2IyYjU3ZmE5IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InVzZXJAZ21haWwuY29tIiwibmJmIjoxNzM3MzMyOTMwLCJjc3JmIjoiNzRjN2YzMDctZjAxMy00NDBhLTk4MmQtOWJhNTZiNmY3MzAzIiwiZXhwIjoxNzM3MzM0NzMwfQ.oDcrt_VcY4I4sq1FnUZeNIOeFaBGn2e7_sfG5YyL9b8"
      ```

4. **GET `/importacao`**
   - Descrição: Retorna dados de importação que podem ser classificados em: `vinhos de mesa`, `espumantes`, `uvas frescas`, `uvas passas` e `suco de uva`.

   - Parâmetros:
     - `ano`: Filtra os dados pelo ano, que deve ser um valor entre 1970 a 2023. Caso esse parâmetro seja omitido, será considerado o ano de 2023.

     - `subopc`: Seleciona uma das opções. Esse parâmetro pode ter os seguintes valores: `vinhos_mesa`, `espumantes`, `uvas_frescas`, `uvas_passas` e `suco_uva`.

   - Retorno: JSON contendo os dados da tabela.

   - Exemplo de uso:
      ```bash
      curl "http://localhost:5000/importacao?ano=2008&subopc=suco_uva" -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTczNzMzMjkzMCwianRpIjoiMzBmODgxNDItMDgyZS00ZDFkLTkxMTAtNGI1N2IyYjU3ZmE5IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InVzZXJAZ21haWwuY29tIiwibmJmIjoxNzM3MzMyOTMwLCJjc3JmIjoiNzRjN2YzMDctZjAxMy00NDBhLTk4MmQtOWJhNTZiNmY3MzAzIiwiZXhwIjoxNzM3MzM0NzMwfQ.oDcrt_VcY4I4sq1FnUZeNIOeFaBGn2e7_sfG5YyL9b8"
      ```


5. **GET `/exportacao`**
   - Descrição: Retorna dados de exportação que podem ser classificados em: `vinhos de mesa`, `espumantes`, `uvas frescas` e `suco de uva`.

   - Parâmetros:
     - `ano`: Filtra os dados pelo ano, que deve ser um valor entre 1970 a 2023. Caso esse parâmetro seja omitido, será considerado o ano de 2023.

     - `subopc`: Seleciona uma das opções. Esse parâmetro pode ter os seguintes valores: `vinhos_mesa`, `espumantes`, `uvas_frescas` e `suco_uva`.

   - Retorno: JSON contendo os dados da tabela.

   - Exemplo de uso:
      ```bash
      curl "http://localhost:5000/exportacao?ano=2020&subopc=espumantes" -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTczNzMzMjkzMCwianRpIjoiMzBmODgxNDItMDgyZS00ZDFkLTkxMTAtNGI1N2IyYjU3ZmE5IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InVzZXJAZ21haWwuY29tIiwibmJmIjoxNzM3MzMyOTMwLCJjc3JmIjoiNzRjN2YzMDctZjAxMy00NDBhLTk4MmQtOWJhNTZiNmY3MzAzIiwiZXhwIjoxNzM3MzM0NzMwfQ.oDcrt_VcY4I4sq1FnUZeNIOeFaBGn2e7_sfG5YyL9b8"
      ```


6. **POST `/signup`**
   - Descrição: Faz o cadastro do usuário para que ele possa usar a API, deve-se passar os campos `email` e `password` em um JSON que vai no corpo da solicitação.

   - Retorno: Um JSON com uma mensagem informando se foi ou não possível cadastrar o usuário.

   - Exemplo de uso:
      ```bash
      curl -X POST http://localhost:5000/signup -H "content-type: application/json" -d '{"email": "user@gmail.com", "password": "12345678"}'
      ```


7. **POST `/signin`**
   - Descrição: Faz o login do usuário, fornecendo-lhe um access token que tem duração por 30 minutos, esse access token vai ser necessário para fazer requisições a todas as rotas GET da API.

   - Retorno: Um JSON com o access token do usuário.

   - Exemplo de uso: 
      ```bash
      curl -X POST http://localhost:5000/signin -H "content-type: application/json" -d '{"email": "user@gmail.com", "password": "12345678"}'
      ```

## TECNOLOGIAS USADAS
Foram usadas as seguintes tecnologias para a construção e implantação dessa API:
   - [Flask](https://flask.palletsprojects.com/en/stable/)
   - [Docker](https://www.docker.com/)
   - [sqlite3](https://www.sqlite.org/)
   - [render](https://render.com/)
   - [JWT](https://jwt.io/)
   - [Beautiful Soup](https://pypi.org/project/beautifulsoup4/)
