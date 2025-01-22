import pytest
from flask import Flask
from flask_restx import Api
from app.routes.scientist_crud import scientist_api
from app.services.scientist_service import (
    get_all_scientists, get_scientist_by_id, create_scientist, update_scientist, delete_scientist
)

# Simulation of the database service
def mock_get_all_scientists():
    """
        Return a list of scientists
    """
    return [
         {
            "id": 1,
            "name": "Marie Curie",
            "birthday": "1867-11-07",
            "description": "Pioneer in radioactivity research",
            "area": "Physics"
        },
        {
            "id": 2,
            "name": "Albert Einstein",
            "birthday": "1879-03-14",
            "description": "Developed the theory of relativity",
            "area": "Physics"
        }
    ]

def mock_get_scientist_by_id(id):
    """
        Return a scientist by ID
    """
    if id == 1:
        return (1, 'Marie Curie', '1867-11-07', 'Pioneer in radioactivity research', 'Physics')
    return None

def mock_create_scientist(name, birthday, description, area):
    """
        Create a new scientist
        Return the ID of the new scientist
    """
    return 3  # New ID

def mock_update_scientist(id, name, birthday, description, area):
    """
        Update a scientist
    """

def mock_delete_scientist(id):
    """
        Delete a scientist
    """


# test client fixture
@pytest.fixture
def client():
    """
        Test client fixture
    """
    app = Flask(__name__)
    app.config['TESTING'] = True
    api = Api(app)
    api.add_namespace(scientist_api)
    with app.test_client() as client:
        yield client


# services mocking
@pytest.fixture(autouse=True)
def mock_services(monkeypatch):
    """
        Mock the services
    """
    monkeypatch.setattr('app.services.scientist_service.get_all_scientists',
                        mock_get_all_scientists)
    monkeypatch.setattr('app.services.scientist_service.get_scientist_by_id',
                        mock_get_scientist_by_id)
    monkeypatch.setattr('app.services.scientist_service.create_scientist',
                        mock_create_scientist)
    monkeypatch.setattr('app.services.scientist_service.update_scientist',
                        mock_update_scientist)
    monkeypatch.setattr('app.services.scientist_service.delete_scientist',
                        mock_delete_scientist)

#  Tests for the endpoint ScientistList
def test_get_all_scientists(client):
    """
        Test the endpoint /scientists/
        GET method
    """
    response = client.get('/scientists/')
    assert response.status_code == 200
    assert len(response.json) == 2
    assert response.json[0]['name'] == 'Marie Curie'

def test_create_scientist(client):
    """
        Test the endpoint /scientists/
        POST method
    """
    data = {
        'name': 'Isaac Newton',
        'birthday': '1643-01-04',
        'description': 'Mathematician and physicist',
        'area': 'Physics'
    }
    response = client.post('/scientists/', json=data)
    assert response.status_code == 201
    assert response.json['id'] == 3
    assert response.json['name'] == 'Isaac Newton'

# Pruebas para el endpoint Scientist
def test_get_scientist_by_id(client):
    response = client.get('/scientists/2')
    assert response.status_code == 200
    assert response.json['name'] == 'Albert Einstein'

def test_get_scientist_not_found(client):
    response = client.get('/scientists/99')
    assert response.status_code == 404
    assert 'not found' in response.json['message']

def test_update_scientist(client):
    data = {
        'name': 'Albert Einstein',
        'birthday': '1879-03-14',
        'description': 'Updated description',
        'area': 'Physics'
    }
    response = client.put('/scientists/2', json=data)
    assert response.status_code == 200
    assert response.json['description'] == 'Updated description'

def test_delete_scientist(client):
    response = client.delete('/scientists/2')
    assert response.status_code == 200
    assert 'deleted' in response.json['message']
