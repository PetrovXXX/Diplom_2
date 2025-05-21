from faker import Faker

fake = Faker()


class GenerateUserCredentials:
    email = ('Petrov' + fake.lexify(text='????????????') + '@diplom2.com').lower()
    password = fake.lexify(text='????????????')
    name = fake.name()


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
