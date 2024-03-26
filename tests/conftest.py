import os
from dotenv import load_dotenv, find_dotenv

from src.models.db import db_session
from src.models.deporte import DeporteEntity

os.environ['ENV'] = 'test'


def pytest_configure(config):
    env_file = find_dotenv('../.env')
    load_dotenv(env_file)
    cargar_informacion()
    return config


def cargar_informacion():
    print("Cargando información necesaria para ejecutar las pruebas")
    cargar_deportes()


def cargar_deportes():
    deportes = db_session.query(DeporteEntity).all()
    if len(deportes) == 0:
        print("Insertando atletismo y ciclismo en la base de datos")
        deporte_atletismo = DeporteEntity(nombre='Atletismo')
        deporte_ciclismo = DeporteEntity(nombre='Ciclismo')
        db_session.add(deporte_atletismo)
        db_session.add(deporte_ciclismo)
        db_session.commit()
