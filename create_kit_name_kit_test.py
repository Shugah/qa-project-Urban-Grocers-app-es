import sender_stand_request
import configuration
import data
from data import kit_body


# C A M B I O   D E   N O M B R E

    # Función para cambiar el valor del parámetro firstName en el cuerpo de la solicitud
def get_user_body(first_name):
    # Copiar el diccionario con el cuerpo de la solicitud desde el archivo de datos
    body = data.user_body.copy()
    # Se cambia el valor del parámetro firstName
    body["firstName"] = first_name
    # Se devuelve un nuevo diccionario con el valor firstName requerido
    return body


    #Envia solicitud con mi nombre en el JSON
user_body = get_user_body("Honey")
response = sender_stand_request.post_new_user(user_body)
assert response.status_code == 201


                                                # A U T H T O K E N
    #Response busca el authToken y se muestra en consola
token = response.json()["authToken"]
print("Mi token:", token)


                                # K I T   C O N   B O D Y   Y   T O K E N
kit_response = sender_stand_request.post_new_kits(kit_body, token)
assert kit_response.status_code == 201
print("Se creó el kit", kit_response.json())


                                        # H E L P E R   T O K E N
def get_new_token(first_name = "Honey"):
    user_body = get_user_body(first_name)
    response = sender_stand_request.post_new_user(user_body)
    assert response.status_code == 201
    return response.json()["authToken"]


                                                # T E S T S
def test_kit_name_length_1():
    token = get_new_token()
    kit_body = {"name": "a"}
    response = sender_stand_request.post_new_kits(kit_body, token)
    assert response.status_code == 201
    assert response.json()["name"] == "a"


def test_kit_name_length_511():
    token = get_new_token()
    kit_body = {"name":"AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"}
    response = sender_stand_request.post_new_kits(kit_body, token)
    assert response.status_code == 201
    assert response.json()["name"] == "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"


def test_kit_name_length_0():
    token = get_new_token()
    kit_body = { "name": "" }
    response = sender_stand_request.post_new_kits(kit_body, token)
    assert response.status_code == 400
    assert response.json()["name"] == ""


def test_kit_name_length_512():
    token = get_new_token()
    kit_body = {  "name":"AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"}
    response = sender_stand_request.post_new_kits(kit_body, token)
    assert response.status_code == 400
    assert response.json()["name"] == "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"


def test_kit_name_special_characters():
    token = get_new_token()
    kit_body = { "name": "№%@," }
    response = sender_stand_request.post_new_kits(kit_body, token)
    assert response.status_code == 201
    assert response.json()["name"] == "№%@,"


def test_kit_name_spaces():
    token = get_new_token()
    kit_body = {"name": "A Aaa"}
    response = sender_stand_request.post_new_kits(kit_body, token)
    assert response.status_code == 201
    assert response.json()["name"] == " A Aaa "


def test_kit_name_numbers_str():
    token = get_new_token()
    kit_body = {"name": "123"}
    response = sender_stand_request.post_new_kits(kit_body, token)
    assert response.status_code == 201
    assert response.json()["name"] == "123"


def test_kit_name_empty():
    token = get_new_token()
    kit_body = {}
    response = sender_stand_request.post_new_kits(kit_body, token)
    assert response.status_code == 400
    assert response.json()["name"] == {}


def test_kit_name_numbers():
    token = get_new_token()
    kit_body = {"name": 123}
    response = sender_stand_request.post_new_kits(kit_body, token)
    assert response.status_code == 400
    assert response.json()["name"] == 123





