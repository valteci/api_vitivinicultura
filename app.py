from flask import Flask, request, Response, jsonify
from flask_jwt_extended import \
    JWTManager, \
    create_access_token, \
    jwt_required


from data.sqlite import Connection
from src.controller.app_controller import App_controller
import json
import requests
import os
from datetime import timedelta
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


app = Flask(__name__)

conn = Connection()
#app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
app.config['JWT_SECRET_KEY'] = 'SAJDFHASHFASHF8E9YTEFHAOSPD'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=30) 
jwt = JWTManager(app)



@app.route('/signup', methods=['POST'])
def signup():
    try:
        controller = App_controller()
        controller.signup(request, conn)

    except Exception as e:
        return jsonify({'msg': str(e)}), 500

    return jsonify({'msg': 'User registered successfully!'}), 200



@app.route('/signin', methods=['POST'])
def signin():
    try:
        controller = App_controller()
        access_token = controller.signin(request, conn)
        return jsonify(access_token=access_token), 200
        
    except Exception as e:
        return jsonify({'msg': str(e)}), 401



@app.route('/comercializacao', methods=['GET'])
@jwt_required()
def comercializacao():
    try:
        controller = App_controller()
        data = controller.comercializacao(request)
        return data, 200
        
    except Exception as e:
        return jsonify({'msg': str(e)}), 500


@app.route('/producao', methods=['GET'])
@jwt_required()
def producao():
    try:
        controller = App_controller()
        data = controller.producao(request)
        return data, 200
        
    except Exception as e:
        return jsonify({'msg': str(e)}), 500


@app.route('/exportacao', methods=['GET'])
@jwt_required()
def exportacao():
    try:
        controller = App_controller()
        data = controller.exportacao(request)
        return data, 200

    except Exception as e:
        return jsonify({'msg': str(e)}), 500



@app.route('/importacao', methods=['GET'])
@jwt_required()
def importacao():
    try:
        controller = App_controller()
        data = controller.importacao(request)
        return data, 200

    except Exception as e:
        return jsonify({'msg': str(e)}), 500




@app.route('/processamento', methods=['GET'])
@jwt_required()
def processamento():
    ano = request.args.get('ano', type=int)
    ano = ano or 2023
    arg_subopc = request.args.get('subopc', type=str)

    if not arg_subopc:
        return jsonify({'msg': f"The argument 'subopc' is required!"}), 500

    if arg_subopc not in SUB_PROCESSAMENTO.keys():
        return jsonify({'msg': f"The sub-option '{arg_subopc}' does not exist!"}), 500

    subopc = SUB_PROCESSAMENTO[arg_subopc]

    if ano < 1970 or ano > 2023:
        return jsonify({'msg': 'year must be in the range 1970 <= year <= 2023'}), 500

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


