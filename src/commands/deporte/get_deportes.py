from src.models.db import db_session
from src.models.deporte import DeporteEntity, DeporteJsonSchema
from src.commands.base_command import BaseCommand


class GetDeportes(BaseCommand):
    def __init__(self):
        pass

    def execute(self):
        deportes = db_session.query(DeporteEntity).all()
        schema = DeporteJsonSchema(many=True)
        return schema.dump(deportes)
