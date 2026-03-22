from typing import Generator
import os

"""
Отсортируйте список словарей 
[{"name": "Bob", "age": 25}, 
{"name": "Alice", "age": 22}, 
{"name": "Charlie", "age": 30}] по полю age.
"""

info = [{"name": "Bob", "age": 25}, 
        {"name": "Alice", "age": 22}, 
        {"name": "Charlie", "age": 30}
        ]

# info_sorted = sorted(info, key=lambda x: len(x["name"]), reverse=True)

# info_sorted = 

# info.sort(key=lambda x: len(x["name"]), reverse=True)
# print(info)




"""
Напишите генератор even_numbers(n), который поочередно выдает четные числа от 0 до n.
"""

# def even_numbers(n: int) -> Generator:
#     for a in range(1, n + 1):
#         if a % 2 == 0:
#              yield a

# gen = even_numbers(10)

# while True:
#      try:
#         print(next(gen))
#      except StopIteration:
#         break


"""
Создайте функцию read_file(filename), которая открывает файл. 
Обработайте FileNotFoundError, а в блоке finally выведите сообщение "Операция завершена".
"""


# def read_file(filename: str) ->None:
#     if not os.path.exists(filename):
#         return None
    
#     try:
#         with open(filename, mode = "r") as file:
#             content = file.read()

#         print(content)
#     except FileNotFoundError:
#         pass



# read_file("555.txt")


"""
Напишите lambda-функцию, которая принимает два числа и возвращает большее из них.
"""

# print((lambda a, b: max(a, b))(5, 3)) 