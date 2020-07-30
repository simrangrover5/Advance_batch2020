from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("one.html")

@app.route("/home/<name>/")
def home(name):
    return render_template("one.html",n = name) #n = key, name=value
#templates --> one.html
#render_template(define path after templates folder)
#templates --> html --> one.html
#render_template("html/one.html")

@app.route("/home/<name>/<float:m1>/<float:m2>/<float:m3>/")
def marks(name,m1,m2,m3):
    data = {
        "name" : name,
        "science" : m1,
        "maths" : m2,
        "english" : m3
    }
    return render_template("one.html",d=data)  #data left (key) , data right (value)
#jinja --> key, value pair
#python file --> name=simran --> name = key/variable, simran = value
#html file --> {{key}} --> {{name}}
# {% if condition %}  {% if condition %}   {% if condition %}
#  s1                      s1                   s1
#  s2                       s2                  s2
# {% endif %}           {% else %}          {% elif condition %}
#                           s3                     s3
#                           s4               {% elif condition %}
#                       {% endif %}                 s4
#                                             {% else %}
#                                                   s5
#                                              {% endif %}
#{% for i in range(10) %}
#   s1
#   s2
#{% endfor %}
# localhost --> one.html  #no d key no n key
#localhost/home/simran --> one.html + n
#localhost/home/simran/12/12/14 --> one.html + d

app.run(debug=True)