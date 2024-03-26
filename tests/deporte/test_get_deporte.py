import uuid
import json
from src.main import app
from src.models.db import db_session
from src.models.deporte import DeporteEntity


class TestGetDeporte():

    def test_get_deporte(self):
        with app.test_client() as test_client:
            id_atletismo = self._obtener_atletismo()
            response = test_client.get(
                '/gestor-usuarios/deportes?id='+id_atletismo, follow_redirects=True)
            response_json = json.loads(response.data)

            assert response.status_code == 200
            assert 'nombre' in response_json
            assert response_json['nombre'] == 'Atletismo'

    def test_get_deporte_no_existente(self):
        with app.test_client() as test_client:
            id_atletismo = str(uuid.uuid4())
            response = test_client.get(
                '/gestor-usuarios/deportes?id='+id_atletismo, follow_redirects=True)
            response_json = json.loads(response.data)

            assert response.status_code == 404
            assert 'error' in response_json
            assert response_json['error'] == f'El deporte con id {id_atletismo} no existe'

    def test_get_deporte_id_invalido(self):
        with app.test_client() as test_client:
            id_atletismo = 'uuid_invalido'
            response = test_client.get(
                '/gestor-usuarios/deportes?id='+id_atletismo, follow_redirects=True)
            response_json = json.loads(response.data)

            assert response.status_code == 400
            assert 'error' in response_json

    def _obtener_atletismo(self):
        deportes = db_session.query(DeporteEntity).all()

        for item in deportes:
            if item.nombre == 'Atletismo':
                return str(item.id)
