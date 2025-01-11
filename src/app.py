from flask import Flask, request, jsonify
import requests
import os
from scrap_parameters import \
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

        response = requests.get(url, headers=HEADERS, timeout=20)
        response.raise_for_status() # lança exceção se algo deu errado
        return response.text
    except:
        path = os.path.abspath('..') + '/' + SAVING_PATH_COMERCIALIZACAO + '/'
        file_name = f'comercializacao{ano}.html'
        html = open(path + file_name).read()
        return html
    



@app.route('/producao', methods=['GET'])
def producao():
    ano = request.args.get('ano', type=int)
    ano = ano or 2023
    
    # tenta fazer a requisição para o site da embrapa
    try:
        args = f'?opcao={Opcao.PRODUCAO.value}&ano={ano}'
        url = BASE_URL + args

        HEADERS = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
        }

        response = requests.get(url, headers=HEADERS, timeout=20)
        response.raise_for_status() # lança exceção se algo deu errado
        return response.text
    except:
        path = os.path.abspath('..') + '/' + SAVING_PATH_PRODUCAO + '/'
        file_name = f'producao{ano}.html'
        html = open(path + file_name).read()
        return html



@app.route('/exportacao', methods=['GET'])
def exportacao():
    ano = request.args.get('ano', type=int)
    ano = ano or 2023
    arg_subopc = request.args.get('subopc', type=str)
    subopc = SUB_EXPORTACAO[arg_subopc]

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
        return response.text
    except:
        path = os.path.abspath('..') + '/' + SAVING_PATH_EXPORTACAO + f'/{arg_subopc}/'
        file_name = f'{arg_subopc}{ano}.html'
        html = open(path + file_name).read()
        return html



@app.route('/importacao', methods=['GET'])
def importacao():
    ano = request.args.get('ano', type=int)
    ano = ano or 2023
    arg_subopc = request.args.get('subopc', type=str)
    subopc = SUB_IMPORTACAO[arg_subopc]

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
        return response.text
    except:
        path = os.path.abspath('..') + '/' + SAVING_PATH_IMPORTACAO + f'/{arg_subopc}/'
        file_name = f'{arg_subopc}{ano}.html'
        html = open(path + file_name).read()
        return html



@app.route('/processamento', methods=['GET'])
def processamento():
    ano = request.args.get('ano', type=int)
    ano = ano or 2023
    arg_subopc = request.args.get('subopc', type=str)
    subopc = SUB_PROCESSAMENTO[arg_subopc]

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
        return response.text
    except:
        path = os.path.abspath('..') + '/' + SAVING_PATH_PROCESSAMENTO + f'/{arg_subopc}/'
        file_name = f'{arg_subopc}{ano}.html'
        html = open(path + file_name).read()
        return html




