from src.utils.base_command import BaseCommand


class Health(BaseCommand):
    def __init__(self):
        pass

    def handle(self):
        return "pong"
