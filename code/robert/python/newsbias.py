import json
from pprint import pprint
import pandas as pd
import matplotlib.pyplot as plt

allsides = open('allsides.json')

data_allsides = json.load(allsides)

for items in data_allsides:
    if int(items['agree']) >= int(items['disagree']):
        print(f"{items['name']} : {items['bias']} : Community Agrees with Analysis")
    else:
        print(f"{items['name']} : {items['bias']} : Community Disagrees with Analysis")

adfontes_csv = pd.read_csv('adfontes2019.csv')

adfontes_csv.plot(x = 'Hori', y = 'Vert', kind = 'scatter')
plt.show()


for items in adfontes_csv:
    search = input('Name a News Source: *')
    print(adfontes_csv[search])

'''
corr_check1 = input("Let's Compare 2 New's Sources, What's the First one: ")
corr_check2 = input("What's the Second One: ")
adfontes_csv.corr()
var_adfontes = adfontes_csv.var()
print(var_adfontes)
'''