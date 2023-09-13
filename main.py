from flask import Flask, render_template, request
import excuseFactory

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/', methods=["POST"])
def indexWithPost():
    return render_template("index.html", message=excuseFactory.generateExcuse(name=request.args.get("name"), location=request.args.get("l"), pro=request.args.get("pro")))

if __name__ == '__main__':
    app.run()
