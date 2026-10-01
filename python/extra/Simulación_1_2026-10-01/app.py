from flask import Flask
from config import Config
from app.controllers.auth_controllers import auth_bp
from app.controllers.book_controllers import book_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Registrar Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(book_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)