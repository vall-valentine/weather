from flask import Flask, render_template
import pandas as pd
from sqlalchemy import create_engine
from data.__all_models import Temp
from data import db_session
from forms.forms import Form
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'solnyshki_vperyod'


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

    return render_template('grath.html')


# прогноз погоды
@app.route('/cities/<city>/predicts', methods=['GET', 'POST'])
def cur_city_pred(city):
    db_session.global_init("db/database.sqlite")
    session = db_session.create_session()
    form = Form()
    if form.is_submitted():
        q= session.query(Temp).filter(Temp.id == 1).first()
        print(q.date == datetime('2020-01-01 00:00:00.000000'))

        d1 = session.query(Temp).filter(Temp.date == form.data1.data, Temp.city == city).first()
        d2 = session.query(Temp).filter(Temp.date == form.data1.data, Temp.city == city).first()
        temps_data = []
        for i in range(d1.id, d2.id):

            a = session.query(Temp).filter(Temp.id == i).first()
            temps_data.append(tuple(a.id, a.date))
        return render_template('forecast.html', form=form, temps_data=temps_data, city=city)
    return render_template('forecast.html', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')