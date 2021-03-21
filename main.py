from flask import Flask, render_template

from data import db_session

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    db_session.global_init("db/database.sqlite")
    session = db_session.create_session()

    # data = и ваши данные
    # temp = Temp(
    #             day=day,
    #             month=month,
    #             year=year,
    #             temp=temp
    #         )
    # session.add(user)
    # session.commit()
    return render_template('main_page.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')