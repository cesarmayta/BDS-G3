from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1><center>Hola mundo con Flask!</center></h1>"

app.run(debug=True)