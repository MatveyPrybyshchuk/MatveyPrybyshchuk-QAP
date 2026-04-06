from typing import Generator, Callable, Literal
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

# def validate_positive(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         print(f"колличество {len(args) + len(kwargs)}")

#         return result
#     return wrapper

# @validate_positive
# def hello(name1, name2) -> str:
#     return f"Hello {name1} and {name2}"


# print(hello("Matvey", "Mat"))


"""
Создай класс BankAccount с приватным атрибутом __balance. Добавь методы deposit(amount), withdraw(amount) и get_balance(). Реализуй проверку: нельзя снять больше, чем есть на счету.
"""

# from decimal import Decimal

# class MinusBalance(Exception):
#     pass


# class BankAccount:
#     def __init__(self, balance: Decimal = Decimal(0)) -> None:
#        self._balance = balance
    
#     def deposit(self, amount: Decimal) -> Decimal:
#         self._balance += amount
        
#         return self._balance

#     def withdraw(self, amount: Decimal) -> Decimal:
#         if amount > self._balance:
#             raise MinusBalance("Недостаточно средств") 
            
#         self._balance -= amount

#         return self._balance

#     def get_balance(self) -> Decimal:
#         return self._balance
    
# obj = BankAccount()
# obj.deposit(Decimal("5000"))
# obj.withdraw(Decimal("1000.15"))
# print(obj.get_balance())



"""
Создай класс Car с атрибутами brand и speed. 
Добавь метод accelerate(amount), увеличивающий скорость, и brake(amount), уменьшающий (не ниже 0). 
Переопредели метод __str__, чтобы print(car) выводил "Car: Toyota, Speed: 60".
"""

# from decimal import Decimal
# from abc import ABC, abstractmethod

# class AbcCar(ABC):

#     @abstractmethod
#     def accelerate(self, amount: int) -> int:
#         raise NotImplementedError
    
#     @abstractmethod
#     def brake(self, amount: int) -> int:
#         raise NotImplementedError

    
# class Car(AbcCar):
#     def __init__(self, brand: str) -> None:
#         self.brand = brand
#         self.speed = 0

#     def accelerate(self, amount) -> int:
#         self.speed += amount

#         return self.speed
    
#     def brake(self, amount) -> int:
        
#         self.speed -= amount
#         if self.speed < 0:
#             self.speed = 0

#         return self.speed
    

#     def __str__(self) -> str:
#         return f"Car: {self.brand}, Speed: {self.speed}"



# toyota = Car("Toyota")
# toyota.accelerate(100)
# toyota.brake(60)

# print(str(toyota))


"""
Используя @dataclass, создай класс Product с полями name: str, price: Decimal, quantity: int = 0.
Создай несколько обьектов, сравни их через ==, выведи через print и repr.
Добавь метод total_cost(), возвращающий price * quantity
"""

# from dataclasses import dataclass
# from decimal import Decimal

# @dataclass
# class Product:
#     name: str
#     price: Decimal
#     quantity: int = 0

#     def __repr__(self) -> str:
#         return f"{self.name}, {self.price}, {self.quantity}"
    
#     def __str__(self)-> str:
#         return "class product"
    
#     @property
#     def total_cost(self) -> Decimal:
#         return self.price * self.quantity


# p1 = Product("tv", Decimal("500.2"))
# p2 = Product("phone", Decimal("100"), 10)
# p3 = Product("tv", Decimal("500.2"))

# # print(p1 == p3)

# # print(repr(p2))
# # print(p2)

# print(p2.total_cost)


"""
Создай иерархию с множественным наследованием: классы Walker с методом move() -> "Иду пешком",
Driver с методом move() -> @Еду на машине" и Commuter(Waler, Driver). Выведи MRO, обьясни порядок 
поиска метода. добавь свой move() в Commuter, который вызывает оба родительских черех super().
"""

# class Walker:
#     def move(self) -> str:
#         return "Иду пешком"

# class Driver:
#     def move(self) -> str:
#         return "Еду на машине"
    
# class Commuter(Walker, Driver):
#     def move(self) -> str:
#         res1 = super(Walker, self).move()
#         res2 = super(Driver, self).move()
#         return res1 + " " + res2
    

# com = Commuter()

# print(com.move())
# print(Commuter.mro())



"""
Реализай класс Matrix (матрица NxM) с магическими методами __add__ (сложение матриц), __mull__
(умножение матриц), __str__
(красивый вывод строк), __eq__ (сравнение), __getitem__(доступ по индексу m[i][j]).
"""

class Matrix:
    def __init__(self, N: int) -> None:
        self.N = N

    def __add__(self, other: int) -> int:
        return self.N + other
    
    def __mul__(self, other: int) -> int:
        return self.N * other
    
    def __str__(self) -> str:
        return f"Num N = {self.N}"
    
    def __eq__(self, other: int) -> bool:
        return self.N == other
    
    def __getitem__(self, other: int) -> Literal[100]:
        return 100
    
mat = Matrix(14)
print(mat + 10)
print(mat * 2)
print(mat)
print(mat == 2)
print(mat[00])