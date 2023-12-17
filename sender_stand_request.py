import configuration
import requests
import data
def post_new_user():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # подставляем полный url
                         json=data.user_body,  # тут тело
                         headers=data.headers)  # а здесь заголовки

#response = post_new_user();
#print(response.status_code)
#print(response.json())


def post_new_client_kit(authToken, kit_name):
    url = configuration.URL_SERVICE + configuration.CREATE_KIT_PATH
    body = {
        "name": kit_name
    }
    new_headers = data.headers.copy()
    new_headers['Authorization'] = f'Bearer {authToken}'
    return requests.post(url, json=body, headers=new_headers)

