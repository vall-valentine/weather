import pandas as pd
import matplotlib.pyplot as plt
import json


def filter(path):
    file = open(path)
    data = json.load(file)
    file.close()
    for i in range(1, len(data)-1):
        if abs((data[i-1]+data[i+1])/2-data[i]) > 10:
            data[i] = (data[i-1]+data[i+1])/2
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


def makePlot(f):
    filtred = filter(f)
    plt.plot([m for m in range(0, 365)], genAver([prediction(n, filtred)
                                                  for n in range(0, 365)]))  # Ox, Oy
    plt.show()


def makePredictArr(f): 
    filtred = filter(f)
    return genAver([prediction(n, filtred) for n in range(0, 365)])


file = open(r"data\20_years_format\predictions\Южный0.json", "w")
t = str(makePredictArr(r"data\20_years_format\Южный.json"))
file.write(t)