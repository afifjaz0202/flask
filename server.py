from flask import Flask
app = Flask(__name__)

@app.route("/") # Revisit decorators if you unclear of this syntax
def index():
    return '<img src="https://preview.redd.it/gap5ah93ciy11.jpg?auto=webp&s=a4497d2ac778a9d46c0f254bb55ae4b502a60b99" />'

@app.route("/another")
def show():
    return '<h1>Penguin Asscheeks</h1>'

if __name__ == '__main__': # Revisit previous challenge if you're uncertain what this does https://code.nextacademy.com/lessons/name-main/424
    app.run()