import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('sqlite:///db/database.sqlite')

files = ['Алмазный.json', 'Западный.json', 'Курортный.json', 'Лесной.json', 'Научный.json',
         'Полярный.json', 'Портовый.json', 'Приморский.json', 'Садовый.json', 'Северный.json',
         'Степной.json', 'Таежный.json', 'Южный.json']

dates = pd.date_range(start='2000-01-01', periods=7305, freq='D')
# Исключаем високосные "дни"
leap_days = (dates.month == 2) & (dates.day == 29)
dates = dates[~leap_days]

dfs = []
for file in files:
    city = file[:-5]
    df = pd.read_json('data/' + file)
    df.columns = ['temp']

    # Сглаживаем аномалии
    for i in range(df.shape[0]):
        if i == 0 or i == (df.shape[0] - 1):
            continue

        average = (df.iloc[i - 1, 0] + df.iloc[i + 1, 0]) / 2
        if abs(average - df.iloc[i, 0]) > 10:
            df.iloc[i, 0] = average

    # Добавим столбец города
    df['city'] = city
    # Добавим индекс по времени
    df['date'] = dates
    dfs.append(df)

# Слепляем вместе датафреймы
temp_df = pd.concat(dfs, axis=0)
temp_df = temp_df.reset_index(drop=True)
temp_df.to_sql(name='temps', con=engine)