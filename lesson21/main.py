from flask import Flask

app= Flask(__name__)

@app.route("/")
@app.route("/<string:name>")
def index(name:str=""):
    return f"<p><h1>hello , happy new year! {name} !</h1></p>"

@app.route('/hello')
def hello():
    return 'Hello, World'