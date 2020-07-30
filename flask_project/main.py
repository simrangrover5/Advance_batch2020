from flask import Flask,render_template,request,make_response,session,redirect,url_for
import pymysql as sql
import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from random import randint
import os 
import requests
from flask  import jsonify
app = Flask(__name__)
app.secret_key = "pijpieijpipe123456pofjpofjpoejpojjbvuhoijpjlejpo"

@app.route("/")
def index():
    if request.cookies.get("islogin"):
        return render_template("afterlogin.html")
    return render_template("nav.html")

@app.route("/login/")
def login():
    if request.cookies.get("islogin"):
        return render_template("afterlogin.html")
    return render_template("login.html")

@app.route("/afterlogin/",methods=["POST","GET"])
def afterlogin():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":  #{"email":email,"passwd":pass}
        email = request.form.get("email")
        password = request.form.get("passwd")
        if email:
            if password:
                try:
                    db = sql.connect(host="localhost",port=3306,user="root",password="",database="batch7_15")
                except Exception as e:
                    print(e)
                    return render_template("login.html")
                else:
                    cursor = db.cursor()
                    cmd = f"select * from user where email='{email}' and password='{password}'"
                    cursor.execute(cmd)
                    data = cursor.fetchone()
                    #print(data)
                    if data:
                        username = data[2]
                        #resp = make_response(render_template("afterlogin.html")) #make response object and give that page that you want to return if the response object will be returned 
                        #resp.set_cookie("email",email) #email = key, email = value
                        #resp.set_cookie("islogin","true") #islogin key and true value
                        #return resp 
                        session['email'] = email
                        session['islogin'] = "True"
                        return render_template("afterlogin.html",user=username)
                    else:
                        error = "Invalid email or password!!!!"
                        return render_template("login.html",error=error) 
                return f"{email},{password}"
            else:
                error = "Invalid password"
                return render_template("login.html",error=error)
        else:
            error = "Invalid email"
            return render_template("login.html",error=error)
@app.route("/signup/")
def signup():
    return render_template("signup.html")

@app.route("/aftersignup/",methods=["POST","GET"])
def aftersignup():
    if request.method == "POST":
        #print(request.form)
        email = request.form.get("email")
        password = request.form.get("passwd")
        gender = request.form.get("gender")
        
        if email and password:
            try:
                db = sql.connect(host="localhost",port=3306,user="root",password="",database="batch7_15")
            except Exception as e:
                print(e)
                return render_template("signup.html")
            else:
                cursor = db.cursor()
                cmd = f"select * from user where email='{email}'"
                cursor.execute(cmd)
                data = cursor.fetchone()
                if data:
                    error = "Email Already Registered!!!"
                    return render_template("signup.html",error=error)
                else:
                    if len(password)>=8:
                            s = 0
                            l = 0
                            u = 0
                            n = 0
                        #for i in password:
                            for i in password:
                                special = "".join(["@","&","$","*","#","%","!"])
                                if i in special:
                                    s += 1 
                                if i.islower():
                                    l += 1
                                if i.isupper():
                                    u += 1
                                if i.isdigit():
                                    n += 1
                            if s>=1 and l>=1 and u>=1 and n>=1:
                                msg = MIMEMultipart()
                                from_email = "simrangrover5@gmail.com"
                                msg['To'] = email 
                                msg['From'] = "simrangrover5@gmail.com"
                                msg['Subject'] = "Mail for Email Validation"
                                #password = getpass("\n Enter your password : ")
                                passwd= os.environ.get("EMAIL_HOST_PASSWORD")
                                otp = randint(1000,9999)
                                html = f"""
                                <html>
                                <body>
                                <h1 style='color:#123456;font-style:italic'>This is your link for your validation</h1>
                                <a href='http://localhost/emailvalidate/' style='color:coral;'>Client on this link to get your email validation</a>
                                </body>
                                </html>
                                """
                                m=MIMEText(html,"html")  #MIMEText(variable_name,content-type)
                                #for sharing plain content with user here we are using "plain", for html content --> "html"
                                #now add the object m with your message object
                                msg.attach(m)  #attached the message m
                                context = ssl.create_default_context()
                                try:
                                    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as server:
                                        server.login(email,passwd)
                                        server.sendmail(email,email,msg.as_string())
                                except Exception as e:
                                    return ("Error : ",e)
                                else:
                                    session['email'] = email
                                    session['password'] = password
                                    session['gender'] = gender
                                    return render_template("signup.html",error = "Mail Send Successfully!!! Check you mail")
                            else:
                                error = "Incorrect Password"
                                return render_template("signup.html",error=error)
                    else:
                        error = "Incorrect Password"
                        return render_template("signup.html",error=error)

            #return f"Email : {email},Password : {password},Gender : {gender}"
        else:
            error = "Invalid Email or password"
            return render_template("signup.html",error=error)
    else:
        return render_template("signup.html")

@app.route("/logout/")
def logout():
    #resp = make_response(render_template("nav.html"))
    #resp.delete_cookie("islogin")
    #resp.delete_cookie("email")
    #return resp
    del session['email']
    del session['islogin']
    return redirect(url_for("index")) #url_for(func_name)
    #redirect to the url on which index function is running
    #return render_template("nav.html")

@app.route("/emailvalidate/")
def get_user():
    try:
        db = sql.connect(host="localhost",port=3306,user="root",password="",database="batch7_15")
    except Exception as e:
        print(e)
        return render_template("signup.html")
    else:
        cursor = db.cursor()
        email = session.get("email")
        password = session.get("password")
        gender = session.get("gender")
        username = email.split("@")[0]
        cmd = f"insert into user values('{email}','{password}','{username}','{gender}')"
        cursor.execute(cmd)
        db.commit()
        del session['email']
        del session['password']
        del session['gender']
        return render_template("login.html")


@app.route("/weather/",methods=['GET','POST'])
def get_weather():
    if request.method == "GET":
        return render_template("getweather.html")
    elif request.method == "POST":
        city = request.form.get("city")
        key = "e9034b1eee3034977886c9f275b27127"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"
        page = requests.get(url)
        if page.status_code == 200:
            data = page.json()
            temp = round(data['main']['temp'] - 273.15,2)
            temp_max= round(data['main']['temp_max'] - 273.15,2)
            temp_min= round(data['main']['temp_min'] - 273.15,2)
            desc = data['weather'][0]['description']
            country = data['sys']['country']
            humidity = data['main']['humidity']
            icon = data['weather'][0]['icon']
            weather = {
                "temp" : temp,
                "min_temp" : temp_min,
                "max_temp" : temp_max,
                "desc" : desc,
                "country" : country,
                "humidity" : humidity
            }
            return render_template("getweather.html",data=weather,icon=icon)
        else:
            print(page.status_code)
            return render_template("getweather.html")
    else:
        return render_template("afterlogin.html",error="Invalid Method")

@app.route("/api/<city>")
def get_api(city):
    key = "e9034b1eee3034977886c9f275b27127"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"
    page = requests.get(url)
    if page.status_code == 200:
            data = page.json()
            temp = round(data['main']['temp'] - 273.15,2)
            temp_max= round(data['main']['temp_max'] - 273.15,2)
            temp_min= round(data['main']['temp_min'] - 273.15,2)
            desc = data['weather'][0]['description']
            country = data['sys']['country']
            humidity = data['main']['humidity']
            icon = data['weather'][0]['icon']
            weather = {
                "temp" : temp,
                "min_temp" : temp_min,
                "max_temp" : temp_max,
                "desc" : desc,
                "country" : country,
                "humidity" : humidity
            }
            return jsonify(weather)
    
app.run(host="localhost",port=80,debug=True)
#to have validation on password
# 1. len should be greater than 8
# 2. it should have one special character,atleast 1 upper, atleast 1 lower, atleast 1 number
# store password in encrypt form
#passlib, cryptography
#SMTP????
#Aftersignup --> Details (email,password,gender)
#get_user --> cmd --> data insert
#1. encrypt your password and store
#2. send otp/link when user click on forgot password/email validation
#3. write a script for attachment thought smtp and mime
#4. Create a random link using your email 
#email --> encrypt of user and attach that encrpting string in your link
#eg --> localhost/email_validate/email_encrpytion of user
#make a function for link localhost/email_validate/<var>
#check whether the var when you decrypt the your email match or not 
#flaskrestframework --> to make rest api
