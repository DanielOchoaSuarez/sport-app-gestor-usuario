from src.utils.base_command import BaseCommand


class GetDeportes(BaseCommand):
    def __init__(self):
        pass

    def execute(self):
        return [{"id": 1, "nombre": "Futbol"}, {"id": 2, "nombre": "Baloncesto"},   {"id": 3, "nombre": "Tenis"}, {"id": 4, "nombre": "Voleibol"}]
