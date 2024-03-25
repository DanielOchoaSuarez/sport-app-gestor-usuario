import logging
from dotenv import load_dotenv
from flask import Flask, jsonify

from src.errors.errors import ApiError
from src.blueprints.health_blueprint import health_blueprint

# Configuración logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(name)s: %(message)s')


# Cargar variables de entorno desde el archivo .env
loaded = load_dotenv()

# Crear instancia de Flask
app = Flask(__name__)

# Registro de blueprints
app.register_blueprint(health_blueprint, url_prefix='/health')


@app.errorhandler(ApiError)
def handle_exception(err):
    response = {
        "msg": err.description
    }
    return jsonify(response), err.code
