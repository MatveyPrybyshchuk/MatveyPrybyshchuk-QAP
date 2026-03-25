from prints.prints_homework import task_visualization
import os
import datetime
from typing import Callable
from typing import Generator
import math


task = "Используя filter() и lambda, отфильтруйте из списка [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] только нечетные числа."
task_visualization(1, task)


print(list(filter(lambda a: a % 2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) )


task = "Напишите функцию apply_operations(numbers, *operations), " \
"которая принимает список чисел и произвольное количество lambda-функций, " \
"последовательно применяя каждую ко всему списку."
task_visualization(2, task)


def apply_operations(numbers, *operations) -> list:
    result = numbers
    for oper in operations:
        result = list(map(oper, result))
    return result


print(apply_operations([1, 2, 3, 4], lambda a: a + 1, lambda a: a + 1))


task = "Напишите генератор chunked(lst, size), " \
"который разбивает список на куски заданного размера и поочередно их выдает. " \
"Например, chunked([1,2,3,4,5], 2) → [1,2], [3,4], [5]."
task_visualization(3, task)


def chunked(lst: list, size: int) -> Generator:
    for i in range(0, len(lst), size):
        yield lst[i:i + size]

for chunk in chunked([1,2,3,4,5], 2):
    print(chunk)


task = "Напишите генератор prime_numbers(), который бесконечно генерирует простые числа. Выведите первые 20."
task_visualization(4, task)


def prime_numbers() -> Generator:
    n = 2
    while True:
        is_prime = True
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            yield n
        n += 1       

step = prime_numbers()

for _ in range(20):
    print(next(step))


task = "Напишите функцию safe_convert(value, type_func), " \
"которая пытается преобразовать value с помощью переданной функции (например, int, float). " \
"При ошибке возвращает None."
task_visualization(5, task)


def safe_convert(value, type_func):
    try: 
        return type_func(value)
    except Exception:
        return None

print(safe_convert(5, lambda a: int(a)))
print(safe_convert("sd", lambda a: float(a)))


task = "Создайте собственный класс исключения NegativeNumberError. " \
"Напишите функцию sqrt_safe(n), которая считает квадратный корень из числа, " \
"но при отрицательном n выбрасывает NegativeNumberError с понятным сообщением."
task_visualization(6, task)


class NegativeNumberError(Exception):
    pass

def sqrt_safe(n) -> int:
    if n < 0:
        raise NegativeNumberError(f"Negative value: {n}")
    return math.sqrt(n)
       
try:
    print(sqrt_safe(-1))
except NegativeNumberError as error:
    print(error)


task = "Напишите функцию-калькулятор calculator(a, b, op), где op — строка ('+', '-', '*', '/'). "
"Обработайте все возможные исключения: деление на ноль, неизвестная операция, некорректные типы аргументов."
task_visualization(7, task)


def calculator(a, b, op: str):
    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
    }

    if not isinstance(op, str):
        raise TypeError('Operator must be a string')
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError('Not supported datatype of input')
    if op not in operations:
        raise TypeError(f'Unsupportable operation: {op}')
    
    try:
        return operations[op](a, b)
    except ZeroDivisionError:
        raise ZeroDivisionError("Division by zero")
    except OverflowError:
        raise OverflowError("Overflow detected")
    

try:
    print(calculator(1, 0, "/"))
except Exception as e:
    print(e) 
