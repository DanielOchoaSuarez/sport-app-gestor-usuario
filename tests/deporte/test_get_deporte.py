import uuid
import json
import pytest
import logging
from faker import Faker
from src.main import app
from src.models.db import db_session
from src.models.deporte import DeporteEntity


logger = logging.getLogger(__name__)
faker = Faker()


@pytest.fixture(scope="class")
def setup_data():
    logging.info("Inicio TestGetDeporte")
    deporte_random = DeporteEntity(nombre=faker.name())
    db_session.add(deporte_random)
    db_session.commit()
    logging.info('deporte creado: ' + deporte_random.nombre)
    yield deporte_random
    logging.info("Fin TestGetDeporte")
    db_session.delete(deporte_random)
    db_session.commit()


@pytest.mark.usefixtures("setup_data")
class TestGetDeporte():

    def test_get_deporte(self, setup_data: DeporteEntity):
        with app.test_client() as test_client:
            response = test_client.get(
                '/gestor-usuarios/deportes?id='+str(setup_data.id), follow_redirects=True)
            response_json = json.loads(response.data)

            assert response.status_code == 200
            assert 'nombre' in response_json
            assert response_json['nombre'] == setup_data.nombre

    def test_get_deporte_no_existente(self):
        with app.test_client() as test_client:
            id_deporte = str(uuid.uuid4())
            response = test_client.get(
                '/gestor-usuarios/deportes?id='+id_deporte, follow_redirects=True)
            response_json = json.loads(response.data)

            assert response.status_code == 404
            assert 'error' in response_json
            assert response_json['error'] == 'resource_not_found'

    def test_get_deporte_id_invalido(self):
        with app.test_client() as test_client:
            id_deporte = 'uuid_invalido'
            response = test_client.get(
                '/gestor-usuarios/deportes?id='+id_deporte, follow_redirects=True)
            response_json = json.loads(response.data)

            assert response.status_code == 400
            assert 'error' in response_json
