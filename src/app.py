from flask import Flask, request, jsonify
import requests

from scrap_parameters import \
    BASE_URL, \
    Opcao




app = Flask(__name__)

@app.route('/comercializacao', methods=['GET'])
def comercializacao():
    ano = request.args.get('ano', type=int)
    ano = ano or 2023
    
    # tenta fazer a requisição para o site da embrapa
    try:
        args = f'?opcao={Opcao.COMERCIALIZACAO.value}&ano={ano}'
        url = BASE_URL + args

        HEADERS = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
        }
        print(url)
        response = requests.get(url, headers=HEADERS, timeout=20)
        response.raise_for_status() # lança exceção se algo deu errado
        return response.text
    except:
        # Acessa os dados em cache
        pass


    return 'get /comercializacao\n'


@app.route('/producao', methods=['GET'])
def producao():
    ano = request.args.get('ano', type=int)
    if not ano:
        ano = 2023

    return 'get /producao\n'

@app.route('/exportacao', methods=['GET'])
def exportacao():
    ano = request.args.get('ano', type=int)
    subopcao = ''

    return 'get /exportacao\n'

@app.route('/importacao', methods=['GET'])
def importacao():
    ano = request.args.get('ano', type=int)
    subopcao = ''

    return 'get /importacao\n'

@app.route('/processamento', methods=['GET'])
def processamento():
    ano = request.args.get('ano', type=int)
    subopcao = ''

    return 'get /processamento\n'