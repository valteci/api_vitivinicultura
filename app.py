from flask import Flask, request, Response, jsonify
from flask_jwt_extended import JWTManager, jwt_required
from data.sqlite import Connection
from src.controller.app_controller import App_controller
import os
from datetime import timedelta


app = Flask(__name__)

conn = Connection()
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
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
    try:
        controller = App_controller()
        data = controller.processamento(request)
        return data, 200

    except Exception as e:
        return jsonify({'msg': str(e)}), 500


