from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retornar_ola_mundo():
    """
    Esse teste tem 3 etapas (AAA)
    - A: Arrange - Arranjo - Organizar
    - A: Act     - Agir - Executa a coisa (o SUT)
    - A: Assert  - Afirmar - Garanta que A é A
    """

    # Arrange
    client = TestClient(app)

    # Act
    response = client.get('/')

    # Assert
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_html():
    client = TestClient(app)
    response = client.get('/html')
    assert response.status_code == HTTPStatus.OK
    assert '<h1>Olá Mundo!</h1>' in response.text
