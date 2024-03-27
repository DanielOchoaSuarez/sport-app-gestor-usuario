import logging
from flask import Blueprint, request, make_response
from src.commands.deporte.get_deportes import GetDeportes
from src.commands.deporte.get_deporte import GetDeporte
from src.utils.seguridad import token_required

logger = logging.getLogger(__name__)
deporte_blueprint = Blueprint('deportes', __name__)


@deporte_blueprint.route('/', methods=['GET'])
def get_deportes():
    id = request.args.get('id')

    if id is None:
        logger.info('Obteniendo deportes')
        result = GetDeportes().execute()
        return make_response(result, 200)

    else:
        logger.info(f"'Obteniendo deporte por id {id}")
        result = GetDeporte(id).execute()
        return make_response(result, 200)


# BORRAR este código. Ejemplo autenticación, el argumennto email se pasa por el decorador token_required
@deporte_blueprint.route('/sec', methods=['GET'])
@token_required
def get_deportes_seguridad(email):
    logger.info(f'Obteniendo deportes. token de seguridad email: {email}')
    result = GetDeportes().execute()
    return make_response(result, 200)
