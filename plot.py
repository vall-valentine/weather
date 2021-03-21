import pandas as pd
import matplotlib.pyplot as plt
import json


def filter(path):
    file = open(path)
    data = json.load(file)
    file.close()
    print("Ошибки в файле:")
    print("день | ошибка")
    for i in range(1, len(data)-1):
        if abs((data[i-1]+data[i+1])/2-data[i]) > 10:
            data[i] = (data[i-1]+data[i+1])/2
            print(i, data[i])
    return data


def prediction(day, arr):
    # day от 0 до 364
    tmp = []
    for i in range(20):
        tmp.append(arr[day+365*i])
    avg = sum(tmp)/len(tmp)
    return avg


def genAver(arr):
    filtered = arr[0]
    k = 0.05
    data = []
    data.append(arr[0])
    for i in range(0, len(arr)-1):
        filtered = filtered * (1 - k) + arr[i+1] * k
        data.append(round(filtered, 2))
    return data


def makePlot(f, a, b):
    filtred = filter(f)
    plt.plot([m for m in range(a, b)], genAver(filtred)[a:b])  # Ox, Oy
    plt.show()


def makePredictArr(f):
    filtred = filter(f)
    return genAver([prediction(n, filtred) for n in range(0, 365)])


def writeFile():
    file = open(r"data\20_years_format\predictions\Южный0.json", "w")
    t = str(makePredictArr(r"data\20_years_format\Южный.json"))
    file.write(t)


def prognoz(f, a, b):
    file = open(f)
    data = json.load(file)
    file.close()
    print("день | температура")
    for i in range(a, b):
        print(i, data[i], sep="     ")
    print("Построить график по этому промежутку?")
    if input("(да / нет): ") == "да":
        makePlot(f, a, b)


# первый параметр - файл по которому строится график
# второй параметр для года 365, для всего промежутка 7300
# makePlot(r"data\20_years_format\Южный.json", 7300)

def main():
    print("Вы хотите построить график по историческим данным или посмотреть прогноз?")
    t = input("(график / прогноз): ")
    if t == "график":
        addr = input("Ведите название города для построения графика: ")
        print("построить график за год или за весь период измерений?")
        t = input("(год / период): ")
        if t == "период":
            a = 0
            b = 7300
        elif t == "год":
            a = (int(input("Введите начальный год (от 1 до 20): "))-1)*365
            b = a+365
        addr = str("data/") + str(addr) + str(".json")
        makePlot(addr, a, b)
    elif t == "прогноз":
        addr = input("Ведите название города: ")
        a = int(input("Введите первый день интервала (>= 0): "))
        b = int(input("Введите последний день интервала (<= 365): "))
        addr = str("data/predictions/") + str(addr) + str("0.json")
        prognoz(addr, a, b)
    else:
        print("Неправильный формат ввода.")
    print()


while True:
    main()
