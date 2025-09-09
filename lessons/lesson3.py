# # Инкапсуляция
# # # Когда имя атрибута или метода начинается с одного подчеркивания (например, _balance),
# # # это обозначает, что он защищен
# # # или может начитаться с двух подчеркиваний (__balance), что обозначает, что он приват
#
#
# class BankAccount:
#
#     def __init__(self, login, password, balance):
#         self.login = login
#         self._balance = balance # защищен
#         self.__password = password # приват
#
#
#     def check_balance(self, password):
#         if password == self.__password:
#             print(self._balance)
#         else:
#             print('Не правельный пароль!!')
#
#
#     def __reset_def_pass(self):
#         self.__password = 123
#
#     def reset_pass(self, password):
#         if password == self.__password:
#             self.__reset_def_pass()
#             print("Пароль сброшен!!")
#         else:
#             print('Не правельный пароль!!')
#
#
# user_1 = BankAccount('Ardager', "123321", 1000)
#
# # user_1.reset_pass("123321")
#
# print(dir(user_1))




# # Абстракция позволяет сосредоточиться на общих характеристиках, скрывая детали
# # реализации. Это можно сделать, создавая абстрактные классы, которые определяют
# # интерфейс (методы) для классов-наследников. В Python абстрактные классы обычно
# # создаются с помощью модуля abc.



from abc import ABC, abstractmethod

# Абстрактный класс
class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass


# class Dog(Animal):
#
#     def __init__(self, name):
#         self.name = name
#
#     def make_sound(self):
#         print(f"{self.name} gaf gaf")
#
#     def move(self):
#         print(f"{self.name} step")
#
# class Cat(Animal):
#
#     def __init__(self, name):
#         self.name = name
#
#     def make_sound(self):
#         print(f"{self.name} kiti kiti")
#
#     def move(self):
#         print(f"{self.name} step")
#
# gufi = Dog("Gufi")


class SendSms(ABC):

    @abstractmethod
    def send_otp(self):
        pass


class KRSendSms(SendSms):

    def send_otp(self):
        msg = f"<text>123321<text/><phone>+996779<phone/>"

        pass

class RSSendSms(SendSms):

    def send_otp(self):
        msg = {
            "text": "text",
            "phone": "+996779"
        }



