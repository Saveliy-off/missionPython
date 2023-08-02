class User:
    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age

class CheckYear(User):
    # Создай функцию которая будет проверять возраст юзера, если < 18 то False, если >= 18 то True
    def checkyear(self):
        pass


test_1 = CheckYear(username='Алекс', age=18)
test_1.checkyear()

test_2 = CheckYear(username='Боб', age=25)
test_2.checkyear()

test_3 = CheckYear(username='Юджин', age=14)
test_3.checkyear()
