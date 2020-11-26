import datetime
import os
from flask import Flask, request, jsonify
from multiprocessing import Process

from src.calc import run_task
from src.db import init_db, insert_into_db, get_result


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    init_db(app.instance_path)

    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    @app.route('/chess', methods=['POST'])
    def calc():
        content = request.get_json()
        n = content['n']
        piece = content['chessPiece']
        id = piece + '_' + str(n)
        result = get_result(app.instance_path, id)
        if result is not None:
            return f'Result for {id} is {result}'
        print(f"***Job started with id = {id} @{datetime.datetime.now()}")
        insert_into_db(app.instance_path, str(id), 'RUNNING...')
        _task = Process(
            target=run_task,
            args=(n, n, piece, str(id), app.instance_path),
            kwargs={"main_task": True}
        )
        _task.start()
        return f'Use this id to retrieve the result: {id}'

    @app.route('/result', methods=['GET'])
    def result():
        id = request.args.get('id')
        result = get_result(app.instance_path, id)
        return f'Result for {id} is {result}'

    return app
