import pytest
import requests
import json


def test_login_valid():
    url = 'https://reqres.in/api/login'
    data = {"email": "peter@klaven","password": " "}
    response = requests.post(url,data=data)
    token = json.loads(response.text)
    assert response.status_code == 200
    assert token['error'] == "user not found"



