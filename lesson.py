from typing import Generator, Callable
import os

"""
Отсортируйте список словарей 
[{"name": "Bob", "age": 25}, 
{"name": "Alice", "age": 22}, 
{"name": "Charlie", "age": 30}] по полю age.
"""

# info = [{"name": "Bob", "age": 25}, 
#         {"name": "Alice", "age": 22}, 
#         {"name": "Charlie", "age": 30}
#         ]

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


"""
Напишите рекурсивную функцию sum_digits(n), которая принимает целое число и возвращает сумму его цифр. Например, sum_digits(123) → 6.
"""
# class NegativeNumberError(Exception):
#     pass


# def sum_digits(n: int) -> int:
#     if n < 0:
#         raise NegativeNumberError(f"Negative value: {n}")
    
#     if n == 0: # 123 12 1 0
#         return 0

#     return n % 10 + sum_digits(n//10) # 3 2 1


# print(sum_digits(-55))


"""
Напишите функцию make_adder(n), которая возвращает функцию, прибавляющую n к любому числу. Например, add5 = make_adder(5), затем add5(10) → 15.
"""

# def make_adder() -> Callable[[int], int]:
#     summ = 0
#     def inner(x: int) -> int:
#         nonlocal summ

#         summ += x

#         return summ

#     return inner


# print(make_adder(10))

"""
Напишите декоратор @uppercase, который преобразует возвращаемую строку функции в верхний регистр.
"""

# def uppercase(func: Callable[[], str]) -> Callable:
#     def inner(*args, **kwargs) -> str:
#         result = func(*args, **kwargs)
#         return result.upper()
    
#     return inner


# @uppercase
# def return_string():
#     return "eeeee"

# print(return_string())



"""
Напишите декоратор @validate_positive, который проверяет, что все аргументы функции — положительные числа. Если нет — бросает ValueError с понятным сообщением.
"""

def validate_positive(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"колличество {len(args) + len(kwargs)}")

        return result
    return wrapper

@validate_positive
def hello(name1, name2) -> str:
    return f"Hello {name1} and {name2}"


print(hello("Matvey", "Mat"))
