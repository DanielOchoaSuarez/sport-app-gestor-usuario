from src.utils.base_command import BaseCommand


class Health(BaseCommand):
    def __init__(self):
        pass

    def execute(self):
        return "pong"