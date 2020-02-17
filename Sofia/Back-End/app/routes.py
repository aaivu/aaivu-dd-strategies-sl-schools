from app import app
import json
import app.users.users as user_model

from bson.json_util import dumps
from flask import request, send_from_directory


# @app.route('/')
# @app.route('/index')
# def index():
#     return "Hi, Hello world..!"


@app.route('/api/user/create', methods=['POST'])
def create_user():
    result = user_model.create_user(json.loads(request.data))
    return dumps(result)


@app.route('/api/user/login', methods=['POST'])
def login_user():
    data = user_model.login_user(json.loads(request.data))
    return dumps(data)


@app.route('/api/user/data/update', methods=['POST'])
def update_data():
    return dumps(user_model.update_data(json.loads(request.data)))


@app.route('/api/user/data/analytics', methods=['POST'])
def run_analysis():
    return dumps(user_model.run_analysis(json.loads(request.data)))

@app.route('/api/user/teacher/getdata', methods=['GET'])
def get_teacher_data():
    return dumps(user_model.get_teacher_data())

@app.route('/')
def send_index():
    return send_from_directory('app/public/', 'index.html')
