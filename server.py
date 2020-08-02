from flask import Flask, render_template
app = Flask(__name__)

@app.route("/") # Revisit decorators if you unclear of this syntax
def index():
    return render_template('index.html') # by default looks for index.html inside a templates folder in the same directory as this script.

@app.route("/surprise")
def show():
    return '<h1>Penguin Asscheeks</h1>'

@app.route("/<name>")
def user(name):
    name = name.upper()
    return render_template('index.html', name=name)

@app.route("/login")
def login():
    signed_in = True # we are hardcoding this just to demonstrate how we can do conditionals in our template files, in future we won't be hardcoding this.
    return render_template('index.html', signed_in=signed_in)

if __name__ == '__main__': # Revisit previous challenge if you're uncertain what this does https://code.nextacademy.com/lessons/name-main/424
    app.run(debug = True)