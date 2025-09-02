
# HeroMag       - heroMage
# hero_kirito      - CONST = 123

class Hero:

    # Конструктор класса
    def __init__(self, name, lvl, hp):
        # Атрибута класса
        self.name = name
        self.lvl = lvl
        self.hp = hp

    # Метод класса
    def action(self):
        print("Base action")

# Объект|Экземпляр класса
kirito = Hero("Kirito", 100, 1000)
asuna = Hero("Asuna", 100, 1000)

text_1 = "text1"
text_2 = "text2"

print(kirito.name)
print(asuna.name)
print(text_1)
print(text_2)



# print(kirito.hp_1)
# kirito.action()

# print(type(kirito))
# print(type("str"))
# print(type(123))
# print(type(12.12))
# print(type([True]))
# print(type({}))
# print(type(()))

# test = []

# kirito.action()

import random