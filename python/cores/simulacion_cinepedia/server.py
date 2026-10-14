import os
from flask_app import app

#importamos rutas registradas
from flask_app.controllers import usuario, Peliculas, comentarios

if __name__ == "__main__":
    #lee el puerto y el modo de depuracion
    port = int(os.getenv("PORT", 5000))
    debug = os.getenv("DEBUG", "True").lower() in ["true", "1", "yes"]

    #levanta el servidor
    app.run(debug=debug, port=port)