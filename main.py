from os import name
from flask import Flask, app,render_template,request
from zope.interface.interface import Method

app = Flask(__name__)

@app.route("/")
@app.route("/home")

def home():
    return render_template("index.html")

@app.route("/result",methods=['POST',"GET"])
def result():
    output= request.form.to_dict()
    name=output["name"]

    return render_template("index.html",name)

if __name__=='__main__':
    app.run(debug= True,port=5001)