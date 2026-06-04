import pytest
import requests
import logging

BASE_URL = "http://jsonplaceholder.typicode.com" 

@pytest.fixture
def api_client():
    session = requests.Session()
    logging.info("Session dibuat")
    yield session
    session.close()
    logging.info("Session ditutup")

@pytest.fixture
def user_data(api_client):
    response = api_client.get(f"{BASE_URL}/users/1")
    return response.json()

