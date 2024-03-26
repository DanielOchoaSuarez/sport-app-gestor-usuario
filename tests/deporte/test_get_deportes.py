import json
from src.main import app


class TestGetDeportes():

    def test_get_deportes(self):
        with app.test_client() as test_client:
            response = test_client.get(
                '/gestor-usuarios/deportes', follow_redirects=True)
            response_json = json.loads(response.data)

            assert response.status_code == 200
            assert len(response_json) >= 2
