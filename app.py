from flask import Flask, request, Response, jsonify
from flask_jwt_extended import \
    JWTManager, \
    create_access_token, \
    jwt_required, \
    get_jwt_identity

from dotenv import load_dotenv
import json
import requests
import os
from src.scraping.scrap import Scraping
from src.scrap_parameters import \
    BASE_URL, \
    Opcao, \
    SAVING_PATH_COMERCIALIZACAO, \
    SAVING_PATH_PRODUCAO, \
    SAVING_PATH_EXPORTACAO, \
    SAVING_PATH_IMPORTACAO, \
    SAVING_PATH_PROCESSAMENTO, \
    SUB_EXPORTACAO, \
    SUB_IMPORTACAO, \
    SUB_PROCESSAMENTO


load_dotenv()
app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'asdfasdfasdfasfd'
jwt = JWTManager(app)


@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username == 'admin' and password == '123':
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200

    return jsonify({"msg": "Usuário ou senha inválidos"}), 401


@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logge_in_as=current_user), 200


@app.route('/comercializacao', methods=['GET'])
def comercializacao():
    ano = request.args.get('ano', type=int)
    ano = ano or 2023
    html = ''
    # tenta fazer a requisição para o site da embrapa
    try:
        args = f'?opcao={Opcao.COMERCIALIZACAO.value}&ano={ano}'
        url = BASE_URL + args

        HEADERS = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
        }

        response = requests.get(url, headers=HEADERS, timeout=20)
        response.raise_for_status() # lança exceção se algo deu errado
        html = response.text
    except:
        path = SAVING_PATH_COMERCIALIZACAO + '/'
        file_name = f'comercializacao{ano}.html'
        html = open(path + file_name).read()
    
    scrap = Scraping()
    data = scrap.extrac_table(html)
    response_data = json.dumps(data, ensure_ascii=False)
    return Response(response_data, status=200, mimetype='application/json')



@app.route('/producao', methods=['GET'])
def producao():
    ano = request.args.get('ano', type=int)
    ano = ano or 2023
    html = ''
    # tenta fazer a requisição para o site da embrapa
    try:
        args = f'?opcao={Opcao.PRODUCAO.value}&ano={ano}'
        url = BASE_URL + args

        HEADERS = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
        }

        response = requests.get(url, headers=HEADERS, timeout=20)
        response.raise_for_status() # lança exceção se algo deu errado
        html = response.text
    except:
        #print(f'{os.path.abspath('.')}')
        path = SAVING_PATH_PRODUCAO + '/'
        file_name = f'producao{ano}.html'
        html = open(path + file_name).read()

    
    # scraping!
    scrap = Scraping()
    data = scrap.extrac_table(html)
    response_data = json.dumps(data, ensure_ascii=False)
    return Response(response_data, status=200, mimetype='application/json')



@app.route('/exportacao', methods=['GET'])
def exportacao():
    ano = request.args.get('ano', type=int)
    ano = ano or 2023
    arg_subopc = request.args.get('subopc', type=str)
    subopc = SUB_EXPORTACAO[arg_subopc]
    html = ''
    try:
        url_skeleton    = BASE_URL + '?opcao={}&ano={}&subopcao={}'
        opcao           = Opcao.EXPORTACAO.value
        url             = url_skeleton.format(opcao, ano, subopc)    

        HEADERS = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/131.0.0.0 Safari/537.36"
            )
        }

        response = requests.get(url, headers=HEADERS, timeout=20)
        response.raise_for_status()
        html = response.text
    except:
        path = SAVING_PATH_EXPORTACAO + f'/{arg_subopc}/'
        file_name = f'{arg_subopc}{ano}.html'
        html = open(path + file_name).read()
        
    scrap = Scraping()
    data = scrap.extrac_table(html)
    response_data = json.dumps(data, ensure_ascii=False)
    return Response(response_data, status=200, mimetype='application/json')


@app.route('/importacao', methods=['GET'])
def importacao():
    ano = request.args.get('ano', type=int)
    ano = ano or 2023
    arg_subopc = request.args.get('subopc', type=str)
    subopc = SUB_IMPORTACAO[arg_subopc]
    html = ''
    try:
        url_skeleton    = BASE_URL + '?opcao={}&ano={}&subopcao={}'
        opcao           = Opcao.IMPORTACAO.value
        url             = url_skeleton.format(opcao, ano, subopc)    

        HEADERS = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/131.0.0.0 Safari/537.36"
            )
        }

        response = requests.get(url, headers=HEADERS, timeout=20)
        response.raise_for_status()
        html = response.text
    except:
        path = SAVING_PATH_IMPORTACAO + f'/{arg_subopc}/'
        file_name = f'{arg_subopc}{ano}.html'
        html = open(path + file_name).read()
    
    scrap = Scraping()
    data = scrap.extrac_table(html)
    response_data = json.dumps(data, ensure_ascii=False)
    return Response(response_data, status=200, mimetype='application/json')



@app.route('/processamento', methods=['GET'])
def processamento():
    ano = request.args.get('ano', type=int)
    ano = ano or 2023
    arg_subopc = request.args.get('subopc', type=str)
    subopc = SUB_PROCESSAMENTO[arg_subopc]
    html = ''
    try:
        url_skeleton    = BASE_URL + '?opcao={}&ano={}&subopcao={}'
        opcao           = Opcao.PROCESSAMENTO.value
        url             = url_skeleton.format(opcao, ano, subopc)    

        HEADERS = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/131.0.0.0 Safari/537.36"
            )
        }

        response = requests.get(url, headers=HEADERS, timeout=20)
        response.raise_for_status()
        html = response.text
    except:
        path = SAVING_PATH_PROCESSAMENTO + f'/{arg_subopc}/'
        file_name = f'{arg_subopc}{ano}.html'
        html = open(path + file_name).read()
    
    scrap = Scraping()
    data = scrap.extrac_table(html)
    response_data = json.dumps(data, ensure_ascii=False)
    return Response(response_data, status=200, mimetype='application/json')




