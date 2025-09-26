from itertools import count


class Money:
    def __init__(self, amount, currency="KGS"):
        self.amount = amount
        self.currency = currency


    def __repr__(self):
        return f"Money {self.amount}"

    def __lt__(self, other):
        return self.amount < other.amount

    def __gt__(self, other):
        print(self.amount)
        print(other.amount)
        return self.amount > other.amount

    def __bool__(self):
        return self.amount != 0


test = Money(100)
test_1 = Money(200)

# print(test > test_1)
# print(bool(Money(0)))
# print(bool(Money(1)))

class Box:
    def __init__(self, *items):
        self.items = list(items)

    def __setitem__(self, idx, value):
        print(idx)
        print(value)
        self.items[idx] = value

    def __getitem__(self, idx):
        return self.items[idx]

box = Box(1,2,3,4,5,6,7,8)

# print(box.items)
# box[1] = 22
# print(box.items)
# print(box[4])

class User:

    def __init__(self, name):
        self.name = name


user = User("Ardager")

class Validate:

    def __init__(self, min_len=3):
        self.min_len = min_len
        self.view = 0
        self.view_user_name = []

    def __call__(self, user):
        if user.name in self.view_user_name:
            return print("no View  added")
        self.view += 1
        self.view_user_name.append(user.name)
        return print("View  added")


# is_ok = Validate()
#
# is_ok(user)
# is_ok(user)
# is_ok(user)
# is_ok(user)
# is_ok(user)
# is_ok(user)
# is_ok(user)
# is_ok(user)
# print(is_ok.view)
# print(is_ok.view_user_name)



def binary_search(array, target):
    left, right = 0, len(array) - 1
    count = 0

    while left <= right:
        count+=1
        # print(count)
        mid = (left + right) // 2
        print(mid)
        if array[mid] == target:
            return print("Найден")
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return print('Не найден!!!!')

my_array = [1,2,3,4,5,6,7,8,9,10,11]

# binary_search(my_array, 10)



# def two_sum(array, target):
#
#     seen = {}
#
#     # range()
#     # len()
#
#     for i in nums:
#         need = target - item
#         if need in seen:
#             return [seen[need], index]
#         seen[item] = index
#
# target = 26
nums = [2,7,11,15]
# print(two_sum(nums, target))

print(range(len(nums)))

for i in range(len(nums)):
    print(i)


# for i, j in enumerate(nums):
#     print(f"{i}, {j}")