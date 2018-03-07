from flask import Flask

import models
from resources.courses import courses_api
from resources.reviews import reviews_api
from resources.forms import forms_api
from flask_cors import CORS


HOST = '0.0.0.0'
PORT = 5000

app = Flask(__name__)
CORS(app)
app.register_blueprint(courses_api)
app.register_blueprint(reviews_api, url_prefix='/api/v1')
app.register_blueprint(forms_api, url_prefix='/api/v1')


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    models.initialize()
    app.run(host=HOST, port=PORT)
