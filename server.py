from flask import Flask, render_template
import random, datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    age= requests.get("https://api.agify.io?name=michael")
    gender = requests.get("https://api.genderize.io?name=peter")
    return render_template("index.html",num=random.randint(1,10),year=datetime.date.today().year)

if __name__=="__main__":
    app.run(debug=True)