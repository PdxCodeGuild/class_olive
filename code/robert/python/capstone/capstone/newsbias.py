import random
import json
from operator import contains
import pandas as pd
import matplotlib.pyplot as plt
import re
from config import token    
import requests

token = token
topheadlinesdata = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={token}").json()
allsides = open('allsides.json')
data_allsides = json.load(allsides)
adfontes_df = pd.read_table('adfontes2019.csv', delimiter=",")
random_list = []
for items in range(0,12):
    random_list.append(random.randint(1,100))

def headlines():

    headline_names = []
    key = 0
    keys_for_headline = []
    headline_urls = []
    headline_opinions = []
    headline_sources = []
    
    for items in range(0,10):
        headline_names.append(topheadlinesdata['articles'][key]['title'])
        headline_urls.append(topheadlinesdata['articles'][key]['url'])
        headline_sources.append(topheadlinesdata['articles'][key]['source']['name'])
        keys_for_headline.append(key)
        key += 1
    
    headline_dict = list(zip(keys_for_headline,headline_names,headline_urls,headline_sources))
    
    for items in headline_dict:
        print(f"{items[0]+1} - {items[1]}")
    
    read_article = input("Type yes if you want to read an article or anything else to go back to the main menu: ").lower()

    while True:
        
        if read_article == 'yes':
            headline_inputted = (int(input("Select the article's number that you want to read: "))-1)
            print(headline_dict[headline_inputted][2])
            read_article = input("Type yes if you want to read an article or anything else to go back to the main menu: ").lower()
        else:
            return False

#community thoughts on ranking
def news_bias():
    menu_options = {
        '1': 'Community Opinions',
        '2': 'News Source Comparison',
        '3': 'All Sources',
        '4': 'Exit'
    }
    print(f"Welcome to the News Bias Analyzer!")

    while True:
        for label,option in menu_options.items():
            print(f'{label} {option}')

        inputted_option = input("\nEnter the number of the action you would like to perform\n ")
        inputted_option = menu_options.get(inputted_option)

        if inputted_option == 'Community Opinions':
           
            community_bias = input(f"Type yes if you want to check a community opinion on the Allsides Data Bias: ")
            if community_bias.lower() == 'yes':
                for items in data_allsides:
                    if int(items['agree']) >= int(items['disagree']):
                        print(f"{items['name']} : {items['bias']} : Community Agrees with Analysis")
                    else:
                        print(f"{items['name']} : {items['bias']} : Community Disagrees with Analysis")
        
        elif inputted_option == 'News Source Comparison':

            compare_bias = 'yes'
            
            while compare_bias == 'yes':
                search_1 = input("Enter the First News Channel(like ABC, Fox, AP, etc) you would like to compare: ")
                search_2 = input("Enter the Second News Channel(like ABC, Fox, AP, etc) you would like to compare: ")

                search_1_plot = adfontes_df[adfontes_df['News'].str.contains(search_1,flags=re.IGNORECASE,regex=True)]
                search_2_plot = adfontes_df[adfontes_df['News'].str.contains(search_2,flags=re.IGNORECASE,regex=True)]

                dataframes = [search_1_plot,search_2_plot]
                search_df = pd.concat(dataframes)
                search_df.plot(x = 'Hori', y = 'Vert', kind = 'scatter', xlabel = 'Political Bias (0 is Base)',ylabel = 'Reliability(30 = Minimal Facts)')
                plt.title("Reliability and Bias Comparison")
                print(search_df)
                x = search_df['Hori'].values.tolist()
                y = search_df['Vert'].values.tolist()
                labels = search_df['News'].values.tolist()
                for item,label in enumerate(labels):
                    plt.annotate(label, (x[item],y[item]))
                plt.show()
                compare_bias = input(f"Type yes if you want to keep searching: ")

        elif inputted_option == 'All Sources':
            adfontes_df.plot(x = 'Hori', y = 'Vert', kind = 'scatter', xlabel = 'Political Bias (0 is Base)',ylabel = 'Reliability(30 = Minimal Facts)')
            plt.title("Reliability and Bias Comparison")
            x = adfontes_df['Hori'].values.tolist()
            y = adfontes_df['Vert'].values.tolist()
            labels = adfontes_df['News'].values.tolist()
            for item,label in enumerate(labels):
                if item in random_list:
                    plt.annotate(label, (x[item],y[item]))
            plt.show()
        
        elif inputted_option == 'Exit':
            print("Thanks for using our News Bias Analyzer!")
            break

        else:
            print("Try again, this doesn't seem to be an option...")

def viewed_topics():
    print(adfontes_df)

'''
Dataframes use this format

dataframe[Header Name][Row Number]
'''
'''

#graphing the datapoints

# News API Time

1. Compare News Channel Bias
2. The Latest News
3. Most Viewed Topics by Bias
'''

def main():
    
    menu_options = {
        '1': 'Compare the News Channel Bias',
        '2': 'Headline News of the Day',
        '3': 'Most Viewed Topics and Bias',
        '4': 'Exit'
    }
    print(f"Welcome to the News Bias Analyzer!")

    while True:
        for label,option in menu_options.items():
            print(f'{label} {option}')

        inputted_option = input("\nEnter the number of the action you would like to perform\n ")
        inputted_option = menu_options.get(inputted_option)

        if inputted_option == 'Compare the News Channel Bias':
            news_bias()

        elif inputted_option == 'Headline News of the Day':
            headlines()

        elif inputted_option == 'Most Viewed Topics and Bias':
            #viewed_topics()
            print("Still being built. Hoping to finish by October, 2022.")

        elif inputted_option == 'Exit':
            print("Thanks for using our News Bias Analyzer!")
            break

        else:
            print("Try again, this doesn't seem to be an option...")

main()