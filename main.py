from flask import Flask, render_template
import pandas as pd
from sqlalchemy import create_engine
from data.__all_models import Temp
from data import db_session
from forms.forms import Form

app = Flask(__name__)


# все города
@app.route('/', methods=['GET'])
@app.route('/cities', methods=['GET'])
def cities():
    return render_template('cities.html')


# график погоды
@app.route('/cities/<city>', methods=['GET'])
def cur_city():
    db_session.global_init("db/database.sqlite")
    session = db_session.create_session()

    return render_template('cur_city.html')


# график погоды
@app.route('/cities/<city>', methods=['GET'])
def cur_city():
    db_session.global_init("db/database.sqlite")
    return render_template('cur_city.html')


# прогноз погоды
@app.route('/cities/<city>/predicts', methods=['GET'])
def cur_city():
    db_session.global_init("db/database.sqlite")
    session = db_session.create_session()
    form = Form
    if form.is_submitted():
        d1 = session.query(Temp).filter(Temp.data == form.data1.data).first()
        d2 = session.query(Temp).filter(Temp.data == form.data2.data).first()
        temps_data = []
        for i in range(d1.id, d2.id):
            a = session.query(Temp).filter(Temp.id == i).first()
            temps_data.append(tuple(a.id, a.date))
        return render_template('forecast.html', temps_data=temps_data)
    return render_template('forecast.html', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')