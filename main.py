from flask import Flask, render_template
import pandas as pd


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


@app.route('/db', methods=['GET'])
def form():
    # Названия файлов
    files = ['Алмазный.json', 'Западный.json', 'Курортный.json', 'Лесной.json', 'Научный.json',
             'Полярный.json', 'Портовый.json', 'Приморский.json', 'Садовый.json', 'Северный.json',
             'Степной.json', 'Таежный.json', 'Южный.json']

    # Считываем все файлы и собираем в 1 Dataframe
    dfs = []
    for file in files:
        city = file[:-5]
        df = pd.read_json(pd.read_json('data/' + file))
        df.columns = [city]
        dfs.append(df)

    temp_df = pd.concat(dfs, axis=1)
    temp_df = temp_df.reset_index(drop=True)

    # Генерируем даты (года 2000-2019)
    dates = pd.date_range(start='2000-01-01', periods=7305, freq='D')
    # Исключаем високосные "дни"
    leap_days = (dates.month == 2) & (dates.day == 29)
    dates = dates[~leap_days]

    # Добавим индекс по времени
    temp_df.index = dates

    for temp in temp_df:
        print(temp)

    return render_template('main_page.html')


if __name__ == '__main__':
    db_session.global_init("db/database.sqlite")
    session = db_session.create_session()



    app.run(port=8080, host='127.0.0.1')