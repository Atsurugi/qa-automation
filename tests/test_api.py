import requests
import pytest
import logging

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.mark.happy_path
def test_status_code_200():
    response = requests.get(f"{BASE_URL}/users/1")
    logging.info(f"URL:{BASE_URL}/users/1")
    logging.info(f"Status Code: {response.status_code}")
    assert response.status_code == 200

@pytest.mark.happy_path
def test_user_punya_field_wajib():
    response = requests.get (f"{BASE_URL}/users/1")
    json_data = response.json()
    logging.info(f"Response Body:{json_data}")
    assert "id" in json_data
    assert "name" in json_data
    assert "email" in json_data
    assert "username" in json_data

@pytest.mark.happy_path
def test_nama_user_benar ():
    response = requests.get(f"{BASE_URL}/users/1")
    json_data = response.json()
    logging.info(f"User Data: {json_data['name']}")
    assert json_data["name"] == "Leanne Graham"

@pytest.mark.negative
def test_user_tidak_ditemukan():
    response = requests.get(f"{BASE_URL}/users/9999")
    logging.info(f"Status Code untuk ID tidak valid: {response.status_code}")
    assert response.status_code == 404

@pytest.mark.happy_path
def test_get_semua_user():
    response = requests.get(f"{BASE_URL}/users")
    json_data = response.json()
    logging.info(f"Jumlah user: {len(json_data)}")
    logging.info(f"User pertama:{json_data[0]['name']}")
    assert response.status_code == 200
    assert len(json_data) == 10
