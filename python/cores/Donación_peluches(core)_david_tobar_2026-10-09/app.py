from flask import Flask
from controllers.auth_controller import auth
from controllers.peluche_controller import peluches

app = Flask(__name__)

app.secret_key = "clave_peluches_123"

app.register_blueprint(auth)
app.register_blueprint(peluches)


if __name__ == "__main__":
    app.run(debug=True)