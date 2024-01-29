from flask import Flask, render_template
import random, datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html",num=random.randint(1,10),year=datetime.date.today().year)

@app.route('/guess/<name>')
def guess(name):
    #name comes from url which gets passed into the function
    age_resposne= requests.get(f"https://api.agify.io?name={name}")
    age_data=age_resposne.json()
    age=age_data["age"]
    gender_response = requests.get(f"https://api.genderize.io?name={name}")
    gender_data=gender_response.json()
    gender=gender_data["gender"]
    return render_template("name.html",year=datetime.date.today().year,person_name=name,age=age,gender=gender)

if __name__=="__main__":
    app.run(debug=True)