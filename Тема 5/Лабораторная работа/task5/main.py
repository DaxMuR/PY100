from random import sample
import string

def get_random_password() -> str:
    a = string.ascii_lowercase
    b = string.ascii_uppercase
    c = string.digits
    d = (a + b + c)
    passwrd = "".join(sample(d, 8))
    return passwrd
     # ...  # TODO написать функцию генерации случайных паролей


print(get_random_password())
