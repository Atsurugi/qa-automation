import requests
import pytest
import logging

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.mark.happy_path
def test_create_post(api_client):
    payload ={
        "title" :  "Belajar QA Automation",
        "body" : "Ini adalah post pertama dari Automation test",
        "userid" : 1
    }
    response = api_client.post(f"{BASE_URL}/posts", json=payload)
    json_data = response.json()
    logging.info(f"Status Code: {response.status_code}")
    logging.info(f"Payload yang dikirim : {payload}")
    logging.info(f"Payload yang di terima: {json_data}")
    assert response.status_code == 201
    assert json_data["title"] == "Belajar QA Automation"
    assert json_data["userid"] == 1
    assert "id" in json_data

@pytest.mark.negative
def test_create_post_tanpa_title(api_client):
    payload = {
        "body" : "Post tanpa title",
        "userid" : 1
    }
    response = api_client.post(f"{BASE_URL}/posts", json=payload)
    json_data = response.json()
    logging.info(f"Status Code: {response.status_code}")
    logging.info(f"Payload yang dikirim: {payload}")
    logging.info(f"Payload yang di terima : {json_data}")
    logging.info(f"Field 'title' ada di response : {'title'in json_data}")
    assert response.status_code == 201
    assert "title" not in json_data

@pytest.mark.happy_path
def test_validasi_body_response_sama_dengan_payload(api_client):
    payload ={
        "body" : "Isi body",
        "userid" : 1
    }
    response = api_client.post(f"{BASE_URL}/posts", json=payload)
    json_data = response.json()
    logging.info(f"Status Code: {response.status_code}")
    logging.info(f"Payload yang dikirim: {payload}")
    logging.info(f"Payload yang di terima : {json_data}")
    logging.info(f"Field 'body' ada di response : {'body' in json_data}")
    assert response.status_code == 201
    assert "body" in json_data

@pytest.mark.negative
def test_payload_kosong(api_client):
    payload ={
    }
    response = api_client.post (f"{BASE_URL}/posts", json=payload)
    json_data = response.json()
    logging.info(f"Status Code : {response.status_code}")
    logging.info(f"Payload yang di kirim: {payload}")
    logging.info(f"Payload yang di terima : {json_data}")
    assert response.status_code == 201
    assert "title" not in json_data
    assert "body" not in json_data
    assert "userid" not in json_data 

