from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

def get_meme():
    #uncomment these two line and comment out the other url line if u want to
    url = "https://official-joke-api.appspot.com/random_joke"
    urldog = "https://dog.ceo/api/breeds/image/random"
    dog = requests.get(urldog)
    joke = requests.get(url)
    img = dog.json()["message"]
    question = joke.json()["setup"]
    answer = joke.json()["punchline"]
    print(dog.json())

    return img,question, answer
    
@app.route("/")
def index():
    img, question, answer = get_meme()
    return render_template("joke.html", img=img, question=question, answer=answer)

app.run(host="0.0.0.0", port=5000, debug=False)