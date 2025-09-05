# # Наследование
# # Родительский|Супер класс
# class BaseUser:
#
#     def __init__(self, name, lvl, hp):
#         self.name = name
#         self.rating = lvl
#         self.password = hp
#
#     def action(self,):
#         print(f"{self.name} Base action")
#
#
# kirito_1 = BaseUser("Kirito 1", 100, 1000)
#
# # Дочерний класс
# class VipUser(BaseUser):
#
#     def cast_spell(self):
#         print(f"{self.name} fire!!!")
#
# class HeroWar(HeroMage):
#     pass
#
#
# kirito = HeroMage("Kirito", 100, 1000)
#
# asuna = HeroWar("Asuna", 199, 1999)



# Полиморфизм
class BaseUser:

    def __init__(self, login, password, user_name):
        self.login = login
        self.password = password
        self.user_name = user_name


    def repost(self, text):
        print(f"{self.user_name} added new repost \n {text}")


class VipUser(BaseUser):

    def __init__(self, login, password, status: list[str], user_name: str ="John Doe"):
        super().__init__(login, password, user_name,)
        self.status = status

    def repost(self, text):
        print(f"{self.user_name} added new repost ❇ ♥ \n {text}")

john = VipUser(password=123321, status=["123"], login="john")
ardager = BaseUser("ardager", 123321, "mr.ardager")
