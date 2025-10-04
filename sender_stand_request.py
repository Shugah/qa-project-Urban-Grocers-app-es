import configuration
import data
import requests

                                                # NUEVO USER
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json = body,
                         headers = data.headers)

    #Marca el status code
response = post_new_user(data.user_body)
print(response.status_code)


                                                # NUEVO KIT
    #Usa el token
def post_new_kits(body, token):
    headers_with_token = {
        "Content-Type": "application/json",
        "Authorization" : "Bearer " + token
    }
    #Hace el kit
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json = body,
                         headers = headers_with_token)

