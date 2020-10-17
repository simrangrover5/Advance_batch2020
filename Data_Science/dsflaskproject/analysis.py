import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests


df = pd.read_csv("../datasets/covid_19_data.csv")

def get_countries():
    c = df['Country/Region'].value_counts().index
    return c

def get_state_df():
    d = requests.get("https://covid-19india-api.herokuapp.com/v2.0/state_data")
    d = d.json()
    states = []
    deaths = []
    recovered = []
    confirmed = []
    rec_rate = []
    death_rate = []
    for i in d[1]['state_data']:
        states.append(i['state'])
        deaths.append(i['deaths'])
        confirmed.append(i['confirmed'])
        recovered.append(i['recovered'])
        rec_rate.append(i['recovered_rate'])
        death_rate.append(i['death_rate'])
    states_df = pd.DataFrame({"States":states,"Confirmed":confirmed,"Deaths":deaths,"Death_Rate":death_rate,"Recover_rate":rec_rate,"Recovered":recovered})
    return states_df
#1. show top 10 countries total recovered
#2. show top 10 countries total confirmed
#3. show top 10 countries total deaths
#api key --> 4b55f36f7bc147b28747111e758d309f