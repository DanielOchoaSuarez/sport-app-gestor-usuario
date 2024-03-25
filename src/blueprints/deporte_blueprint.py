import os
import logging
from flask import Blueprint, jsonify
from src.commands.deporte.get_deportes import GetDeportes

logger = logging.getLogger(__name__)
deporte_blueprint = Blueprint('deportes', __name__)


@deporte_blueprint.route('/', methods=['GET'])
def health():
    logger.info('Obteniendo deportes')
    result = GetDeportes().execute()
    return jsonify(result)
