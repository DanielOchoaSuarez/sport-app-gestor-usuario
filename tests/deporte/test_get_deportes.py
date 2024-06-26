import json
from typing import List
import pytest
import logging
from faker import Faker
from unittest.mock import patch, MagicMock
from src.main import app
from src.models.db import db_session
from src.models.deporte import DeporteEntity


logger = logging.getLogger(__name__)
faker = Faker()


@pytest.fixture(scope="class")
def setup_data():
    logging.info("Inicio TestGetDeportes")
    deporte_random_1 = DeporteEntity(nombre=faker.name())
    deporte_random_2 = DeporteEntity(nombre=faker.name())
    db_session.add(deporte_random_1)
    db_session.add(deporte_random_2)
    db_session.commit()
    lista_deportes: List[DeporteEntity] = [deporte_random_1, deporte_random_2]
    for deporte in lista_deportes:
        logging.info('deporte creado: ' + deporte.nombre)

    yield lista_deportes

    logging.info("Fin TestGetDeportes")
    for deporte in lista_deportes:
        logging.info('deporte eliminado: ' + deporte.nombre)
        db_session.delete(deporte)
    db_session.commit()


@pytest.mark.usefixtures("setup_data")
class TestGetDeportes():

    def test_get_deportes(self, setup_data: List[DeporteEntity]):
        with app.test_client() as test_client:
            response = test_client.get(
                '/gestor-usuarios/deportes', follow_redirects=True)
            response_json = json.loads(response.data)

            assert response.status_code == 200
            assert len(response_json) >= len(setup_data)


# BORRAR este test. Ejemplo del mock de autenticación
@pytest.mark.usefixtures("setup_data")
class TestGetDeportesSec():

    @patch('requests.post')
    def test_get_deportes(self, mock_post, setup_data: List[DeporteEntity]):
        with app.test_client() as test_client:
            mock_response = MagicMock()
            mock_response.status_code = 200
            mock_response.json.return_value = {
                'token_valido': True, 'email': 'test@example.com'}
            mock_post.return_value = mock_response

            headers = {'Authorization': 'Bearer 123'}
            response = test_client.get(
                '/gestor-usuarios/deportes/sec', headers=headers, follow_redirects=True)
            response_json = json.loads(response.data)

            assert response.status_code == 200
            assert len(response_json) >= len(setup_data)
