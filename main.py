from flask import Flask, render_template, request
import excuseFactory
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/', methods=["POST"])
def indexWithPost():
    location = request.form.get("l")
    if request.form.get("l") == None:
        location = ""
    pro = request.form.get("p")
    name = request.form.get("name")

    print(pro)
    print(name)
    print(location)
    return render_template("index.html", message=excuseFactory.generateExcuse(pro, location, name), bustCache=str(random.randint(0,100000000)))

if __name__ == '__main__':
    app.run(port=23873)
