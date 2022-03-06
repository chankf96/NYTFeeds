from flask import Flask, render_template, request
import requests
from model import Article

app = Flask(__name__)

app.debug = True

@app.route('/')
def index():
    art = Article()
    result = art.getArticles()
    return render_template('index.html', data=result)

if __name__ == '__main__':
    app.run()


