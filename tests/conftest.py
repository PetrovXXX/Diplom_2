import pytest
import requests

from faker import Faker
from curl import Urls
from data import IngredientsData
from data import GenerateUserCredentials

faker = Faker()


@pytest.fixture
def generate_user_credentials():
    email = GenerateUserCredentials.get_email()  # Новые данные при каждом вызове
    password = GenerateUserCredentials.get_password()
    name = GenerateUserCredentials.get_name()
    return email, password, name


@pytest.fixture
def create_new_user(generate_user_credentials):
    email, password, name = generate_user_credentials
    payload = {"email": email, "password": password, "name": name}
    response = requests.post(f"{Urls.REGISTER_USER}", data=payload)

    # Проверяем, что пользователь создан успешно
    assert response.status_code == 200, f"Ошибка создания пользователя: {response.text}"
    assert "accessToken" in response.json(), "Токен не получен"

    data = response.json()
    yield [email, password, name], data  # Возвращаем данные для теста

    # Удаление пользователя после теста
    access_token = data["accessToken"]
    requests.delete(f"{Urls.DELETE_USER}", headers={'Authorization': f'{access_token}'})


@pytest.fixture
def create_new_order(create_new_user):
    access_token = create_new_user[1]["accessToken"]
    headers = {"Authorization": f"{access_token}"}
    payload = {
        'ingredients': [IngredientsData.BUN, IngredientsData.SAUCE, IngredientsData.FILLER]
    }
    response = requests.post(f'{Urls.GET_USER_ORDERS}', data=payload, headers=headers)
    data = response.json()
    return data