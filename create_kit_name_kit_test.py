import pytest
import sender_stand_request
import data


@pytest.fixture(scope='session')
def get_new_user_token():
    sender_stand_request.post_new_user()
    response = sender_stand_request.post_new_user()
    return response.json()['authToken']


@pytest.mark.parametrize('name', [
    pytest.param('a', id='1 symbol'),
    pytest.param('AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC', id='511 symbol'),
    pytest.param('QWErty', id='razresh_eng_symbol'),
    pytest.param('Мария', id='razresh_rus_symbol'),
    pytest.param('"№%@",', id='razresh_spec_symbol'),
    pytest.param(' Человек и КО ', id='razresh_probely'),
    pytest.param('123', id='razresh_cyfry'),
])
def test_positive_assert(get_new_user_token, name):
    response = sender_stand_request.post_new_client_kit(get_new_user_token, name)
    assert response.status_code == 201
    assert response.json()['name'] == name


@pytest.mark.parametrize('name',[
    pytest.param('', id='0 symbol'),
    pytest.param('AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD', id="512 symbol"),
    pytest.param(123, id='drugoy_type')
])
def test_negative_assert(get_new_user_token, name):
    response = sender_stand_request.post_new_client_kit(get_new_user_token, name)
    assert response.status_code == 400


def test_negative_assert_no_kit_name(get_new_user_token):
    name = data.kit_body.copy()
    name.pop("name")
    response = sender_stand_request.post_new_client_kit(get_new_user_token,name)
    assert response.status_code == 400







