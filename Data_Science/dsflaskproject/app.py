from flask import Flask,render_template,request,redirect,url_for
from analysis import get_countries
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
import requests
from analysis import get_state_df

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/country/")
def get_update():
    c = get_countries()
    df = pd.read_csv("../datasets/covid_19_data.csv")
    fig,(ax1,ax2,ax3) = plt.subplots(1,3,figsize=(13,5))
    print(fig)
    df.groupby("Country/Region").sum().sort_values(by="Confirmed",ascending=False)['Confirmed'][:10].plot(kind="pie",ax=ax1)
    df.groupby("Country/Region").sum().sort_values(by="Recovered",ascending=False)['Recovered'][:10].plot(kind="pie",ax=ax2)
    df.groupby("Country/Region").sum().sort_values(by="Deaths",ascending=False)['Deaths'][:10].plot(kind="pie",ax=ax3)
    plt.savefig("static/images/pie.png",bbox_inches="tight")
    return render_template("coun.html",country = c,img="pie.png")  #country = key, c = value

@app.route("/getdetails/",methods=['GET','POST'])
def get_details():
    if request.method == "POST":
        c = request.form.get("country")
        mont = request.form.get("month")
        t = request.form.get("type")
        df = pd.read_csv("../datasets/covid_19_data.csv")
        fig = plt.figure(figsize=(11,5),facecolor="black")
        ax = fig.add_axes([0,0,1,1],facecolor="black")
        temp = df[df['Country/Region'] == c]
        v = temp[temp['ObservationDate'].apply(lambda x : True if x.split("/")[0] == (str(mont)) else False)][t].values
        i = temp[temp['ObservationDate'].apply(lambda x : True if x.split("/")[0] == (str(mont)) else False)]['ObservationDate'].values
        sns.barplot(i,v,ax=ax)
        for p,text in zip(ax.patches,v):
            x = p.get_x()
            h = p.get_height() + 0.5
            plt.text(x,h,text,fontsize=10,color="white",rotation=90)
        ax.set_xticklabels(i,rotation=90,color="white")
        ax.set_yticklabels(ax.get_yticks(),color="white")
        plt.savefig(f"static/images/{c}{mont}{t}.png",bbox_inches="tight",dpi=72,facecolor="black")
        return render_template("show.html",total=sum(v),c=c,m=mont,t=t)
    elif request.method == "GET":
        return redirect(url_for("index"))

@app.route("/news/")
def news_update():
    url = ('http://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=4b55f36f7bc147b28747111e758d309f')
    response = requests.get(url)
    if response.status_code == 200:
        all_news = []
        response = response.json()
        for i in response['articles']:
            d = {}
            if i.get("content"):
                if "corona" in i.get("content").lower() or "covid-19" in i.get("content").lower():
                    d['url'] = i['url']
                    d['content'] = i['content']
                    all_news.append(d)
        return render_template("news.html",news=all_news)

@app.route("/state/",methods=['GET','POST'])
def state_updates():
    if request.method == "GET":
        states_df = get_state_df()
        plt.figure(figsize=(11,5))
        sns.barplot(states_df['States'],states_df['Confirmed'])
        plt.tick_params(axis="x",rotation=90)
        plt.savefig("static/images/stateconfirmed.png",bbox_inches="tight")
        plt.figure(figsize=(11,5))
        sns.barplot(states_df['States'],states_df['Recovered'])
        plt.tick_params(axis="x",rotation=90)
        plt.savefig("static/images/staterecover.png",bbox_inches="tight")
        plt.figure(figsize=(11,5))
        sns.barplot(states_df['States'],states_df['Deaths'])
        plt.tick_params(axis="x",rotation=90)
        plt.savefig("static/images/statedeath.png",bbox_inches="tight")
        return render_template("show_states.html",s=states_df['States'])
    else:
        s = request.form.get("state")
        state_df = get_state_df()
        d = state_df[state_df['States'] == s].values[0]
        d1 = {}
        d1['state'] = d[0]
        d1['con'] = d[1]
        d1['death'] = d[2]
        d1['recover'] = d[5]
        return render_template("show_states.html",d=d1,s=state_df['States'])

app.run(host="localhost",port=80,debug=True)