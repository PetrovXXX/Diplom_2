from faker import Faker

import uuid

fake = Faker()

class GenerateUserCredentials:
    @staticmethod
    def get_email():
        return f'petrov_{uuid.uuid4().hex[:8]}@diplom2.com'.lower()

    @staticmethod
    def get_password():
        return fake.lexify(text='????????????')

    @staticmethod
    def get_name():
        return fake.name()


class ExistentUserCredentials:
    email = 'Petrov_17_cogorta@diplom.com'
    wrong_email = 'Petrov_17gruppa@diplom.com'
    password = 'diplompass'
    wrong_password = 'diplompass756%%63'
    name = 'Ilya_17_test_api'


class IngredientsData:
    BUN = '61c0c5a71d1f82001bdaaa6d'
    SAUCE = '61c0c5a71d1f82001bdaaa75'
    FILLER = '61c0c5a71d1f82001bdaaa78'
