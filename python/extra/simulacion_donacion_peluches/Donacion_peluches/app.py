import os
from dotenv import load_dotenv
from flask import Flask
from controllers.auth_controller import auth
from controllers.peluche_controller import peluches

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "clave-local-cambiar")

app.register_blueprint(auth)
app.register_blueprint(peluches)

if __name__ == "__main__":
    app.run(debug=True)
