import requests
import math
import time
from datetime import datetime

response = requests.get('https://or.water.usgs.gov/non-usgs/bes/hayden_island.rain')
text = response.text
with open('hayden_island.txt', 'w') as file:
        file.write(text)
        
    
class dayofrain():
    def __init__(self, date, total):
        self.date = date
        self.total = total
        

def average(x):
    total = 0
    for i in range(len(x)):
        total += x[i]
    return total / len(x)
# print(average([34, 56, 73, 21])) # 46.0

def variance(x):
    mu = average(x)
    total = 0
    for i in range(len(x)):
        total += (x[i] - mu)**2
    return total / len(x)
# print(variance([34, 56, 73, 21])) # 399.5

def standard_deviation(x):
    v = variance(x)
    return math.sqrt(v)
# print(standard_deviation([34, 56, 73, 21])) # 19.987

def getdate(value):
    return datetime.strptime(value, '%d-%b-%Y')

listofdaysofrain = []
daysofrain = []

with open('hayden_island.txt', 'r') as file:
    for index, line in enumerate(file):
        if index> 10:
            try:
                line = file.readline()
                data = line.split()
                date = getdate(data[0])
                total = float(data[1])
                listofdaysofrain.append((date, total))
                daysofrain.append(dayofrain(date, total))
            except:
                pass
            # time.sleep(1)

max = 0
dates = []
totals = []
for r in daysofrain:
    #print(r.date)
    #print(r.total)
    dates.append(r.date)
    totals.append(r.total)
    if r.total > max:
        max = r.total
        print(r.date)
        print(max)
    #time.sleep(1)