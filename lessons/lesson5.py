# # 1. Декоратор @staticmethod
# # Декоратор @staticmethod используется для того, чтобы определить метод, который не зависит от экземпляра класса
# # (не использует self) и не зависит от самого класса (не использует cls). Такой метод можно вызывать без создания
# # экземпляра класса.
#
# class Math:
#
#     def __init__(self, name):
#         self.name = name
#
#     def get_name(self):
#         print(self.name)
#
#     @staticmethod
#     def add(a, b):
#         print(a + b)
#
# obj_1 = Math("Name")
# # obj_1.get_name()
# # Math.add(12,321)
#
#
# # 2. Декоратор @classmethod
# # Описание:
# # Декоратор @classmethod используется для определения метода, который принимает первым аргументом
# # сам класс (не экземпляр). Этот аргумент обычно называется cls. Метод класса может изменять состояние класса,
# #  но не работает с состоянием конкретного экземпляра.
#
# # class Person:
# #
# #     # Атрибут класса
# #     population = 0
# #     math = Math
# #
# #     def __init__(self, name):
# #         # Атрибуты экземпляра|объекта класса
# #         self.name = name
# #         Person.population += 1
# #
# #     def get_name(self):
# #         print("test")
# #
# #     @classmethod
# #     def get_population(cls):
# #         cls.math("Name")
# #         return print(cls.population)
#
# # obj_2 = Person("Name2")
# # obj_3 = Person("Name2")
# #
# # Person.get_population()
#
#
# # 3. Декоратор @property
# # Описание:
# # Декоратор @property используется для того, чтобы метод стал доступным как атрибут, но при этом оставался методом.
# # Это позволяет скрывать логику вычислений или проверки, делая код более чистым. Обычно используется
# # для создания геттеров и сеттеров.
#
#
# class Person:
#
#     def __init__(self, first_name, last_name, bonus_balance, balance):
#         # Атрибуты экземпляра|объекта класса
#         self.first_name = first_name
#         self.last_name = last_name
#         self.bonus_balance = bonus_balance
#         self.balance = balance
#
#     @property
#     def full_name(self):
#         print(f"{self.last_name} {self.first_name}")
#
#     @property
#     def total_balance(self):
#         print(self.bonus_balance + self.balance)
#
#
#
#
# obj_4 = Person("Ardager", "Kartanbekov")
#
# obj_4.full_name
# obj_4.total_balance





#
# @simple_decorator
# def say_hello():
#     print('Hello world')

# say_hello()

def greeting_decorator(func):
    def wrapper(name):
        print(f"Привет {name}!!")
        func(name)
    return wrapper

@greeting_decorator
def greeting(name):
    print(f"Как дела {name} ?")


# greeting("ARDAGER")

def simple_decorator(func):
    def wrapper():
        func()
    return wrapper

def repeat_decorator(n):
    def decorator(func):
        def wrapper():
            print(n)
            func()
        return wrapper
    return decorator

@repeat_decorator(4)
def hello():
    print("hello")

# hello()


def class_decorator(cls):
    class NewClass(cls):
        @staticmethod
        def new_method():
            print("New method!!")

    return NewClass

@class_decorator
class OldClass:
    @staticmethod
    def old_method():
        print("Old method!!")


# obj_8 = OldClass()
# obj_8.new_method()




# class Test:
#
#     # Магический метод
#     def __init__(self, name):
#         self.__name = name
#
#     def __str__(self):
#         return self.__name
#
#     def __gt__(self, other):
#         pass
#
#     def __add__(self, other):
#         pass
#
# test = Test("Name")
# #
# # print(test)
#
# array = [1,2,4,5]
#
# array[0] = 23
# print(test)
#
# # print(dir(test))