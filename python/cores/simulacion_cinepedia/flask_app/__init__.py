import os
from flask import Flask
from dotenv import load_dotenv

#cargar las variables
load_dotenv()

app = Flask(__name__)

#configurar clave secreta
app.secret_key = os.getenv("FLASK_SECRET_KEY", "clave_desarrollo_default")