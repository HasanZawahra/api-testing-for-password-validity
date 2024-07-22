import requests
import pytest
from dataAndFunctions.links import linkes
from dataAndFunctions.data import *

def test_1():
    json = {fields.password : data.not_containing_at_least_2_letters}
    response = requests.post(linkes.login, data=json)
    assert response.status_code == status_codes.OK
    assert data.not_containing_at_least_2_letters_statement in response.text

def test_2():
    json = {fields.password : data.not_containing_at_least_1_number}
    response = requests.post(linkes.login, data=json)
    assert response.status_code == status_codes.OK
    assert data.not_containing_at_least_1_number_statement in response.text

def test_3():
    json = {fields.password : data.not_containing_at_least_1_special_char}
    response = requests.post(linkes.login, data=json)
    assert response.status_code == status_codes.OK
    assert data.not_containing_at_least_1_special_char_statement in response.text

def test_4():
    json = {fields.password : data.short_password}
    response = requests.post(linkes.login, data=json)
    assert response.status_code == status_codes.OK
    assert data.short_password_statement in response.text

def test_5():
    json = {fields.password : data.not_containing_at_least_1_uppercase}
    response = requests.post(linkes.login, data=json)
    assert response.status_code == status_codes.OK
    assert data.not_containing_at_least_1_uppercase_statement in response.text

def test_6():
    json = {fields.password : data.not_containing_at_least_1_lowercase}
    response = requests.post(linkes.login, data=json)
    assert response.status_code == status_codes.OK
    assert data.not_containing_at_least_1_lowercase_statement in response.text

def test_7():
    json = {fields.password : data.long_password}
    response = requests.post(linkes.login, data=json)
    assert response.status_code == status_codes.OK
    assert data.long_password_statement in response.text

def test_8():
    json = {fields.password : data.has_repeated_sequences}
    response = requests.post(linkes.login, data=json)
    assert response.status_code == status_codes.OK
    assert data.has_repeated_sequences_statement in response.text