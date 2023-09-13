from flask import Flask, render_template, request
import excuseFactory
import sys

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/', methods=["POST"])
def indexWithPost():
    print(request.args)
    location = request.args.get("l")
    if request.args.get("l") == None:
        location = ""
    pro = request.args.get("p")
    name = request.args.get("name")
    return render_template("index.html", message=excuseFactory.generateExcuse(pro, location, name))

if __name__ == '__main__':
    app.run()
