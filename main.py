from flask import Flask, render_template
import pandas as pd
from sqlalchemy import create_engine
from data import __all_models
from data import db_session

app = Flask(__name__)


@app.route('/', methods=['GET'])
@app.route('/cities', methods=['GET'])
def cities():
    db_session.global_init("db/database.sqlite")
    session = db_session.create_session()

    return render_template('cities.html')


@app.route('/cities/<city>', methods=['GET'])
def cur_city():
    db_session.global_init("db/database.sqlite")
    session = db_session.create_session()

    return render_template('cur_city.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')