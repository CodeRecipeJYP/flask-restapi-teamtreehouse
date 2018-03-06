from flask import Flask

import models
from resources.courses import courses_api

HOST = '0.0.0.0'
PORT = 5000

app = Flask(__name__)
app.register_blueprint(courses_api)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    models.initialize()
    app.run(host=HOST, port=PORT)
