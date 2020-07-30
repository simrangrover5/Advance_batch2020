from flask import Flask

app = Flask(__name__) #Flask("flask_project")
#__name__ --> space,module
#app object of Flask class of currect space 
#templates --> html --> PWD , Static --> PWD

#development --> localhost --> /
#deployment --> domain --> / --> example.com 
@app.route("/")  #/ --> domain, default --> localhost , / --> localhost : 127.0.0.1
def index():
    return "Hello world"
#if request for / will come the index function will be run

@app.route("/home/<name>/") #localhost/home example.com/home/
def home(name):
    return f"<h1 style='color:red'>Welcome to my home {name}</h1>"

@app.route("/home/<name>/<int:age>/")
def vote(name,age):
    if age>=18:
        return f"<h1 style='color:green'>{name} can vote</h1>"
    else:
        return f"<h1 style='color:green'>{name} cannot vote</h1>"

app.run(host="localhost",port=80,debug=True)
#debug = True --> Show error on browser/client side
#localhost/home/simran --> Welcome simran
#localhost/home/manisha --> Welcome manisha
#localhost/home/harsh --> Welcome harsh  --> variable path
#<var> --> data type --> string default, <int:var> --> var data type integer
#<float : var> --> var data type float
#path --> localhost/simran/50/60/70
#calculate the percentage from my marks and return my grade and percentage
# per<40 --> F
# 40<=per<50 --> E
#90<=per<=100 --> A+
#simran has got 70% and grade B
