import uuid
import logging

from src.errors.errors import BadRequest, ResourceNotFound
from src.models.db import db_session
from src.models.deporte import DeporteEntity, DeporteJsonSchema
from src.commands.base_command import BaseCommand

logger = logging.getLogger(__name__)


class GetDeporte(BaseCommand):
    def __init__(self, id: str):
        self.id = id

    def execute(self):
        self._validateRequest()

        deporte = db_session.query(DeporteEntity).filter(
            DeporteEntity.id == self.id).first()

        if deporte is None:
            err = f"El deporte con id {self.id} no existe"
            logger.error(err)
            raise ResourceNotFound(err)

        schema = DeporteJsonSchema()
        return schema.dump(deporte)

    def _validateRequest(self):
        print('Validando información para consultar deporte por id')

        try:
            uuid.UUID(self.id)
            return
        except ValueError:
            raise BadRequest
