import requests
import pytest
from dataAndFunctions.links import linkes
from dataAndFunctions.data import *

def test_valid_password():
    json = {fields.password : data.valid}
    response = requests.post(linkes.login, data=json)
    assert response.status_code == status_codes.OK
    assert data.valid_statement in response.text