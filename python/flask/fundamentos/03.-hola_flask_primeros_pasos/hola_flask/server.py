from flask import Flask

app = Flask(__name__)

@app.route("/")
def hola_mundo():
    return "¡Hola a todos!"

@app.route("/nosotros")
def nosotros():
    return "¡conocenos un poco mas!"

@app.route("/casino")
def casino():
    return "¡Bienvenidos al casino infernal!"

@app.route("/poker")
def poker():
    return "¡juguemos unas partidas, si pierdes me daras tu alma!"

if __name__ == "__main__":
    app.run(debug=True)