# # class Swim:
# #     def action(self):
# #         print("Swim")
# #
# # class Fly:
# #     def action(self):
# #         print("Fly")
# #
# #
# # class Duck(Swim, Fly):
# #     pass
# #
# #
# # donald_duck = Duck()
# #
# # donald_duck.action()
# # donald_duck.action()
#
#
#
# class A:
#     def action(self):
#         print('A')
#
# class B(A):
#     def action(self):
#         super().action()
#         print('B')
#
# class C(A):
#     def action(self):
#         print('C')
#
# class D(B,C):
#     pass
#     # def action(self):
#     #     print('D')
#
#
# obj = D()
# obj2 = B()
#
# obj2.action()
#
# # Method Resolution Order
# print(D.__mro__)


