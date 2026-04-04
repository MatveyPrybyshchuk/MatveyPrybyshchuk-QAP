from prints.prints_homework import task_visualization
from typing import Callable
import warnings
from functools import wraps

"""

1. Напишите рекурсивную функцию palindrome(s), которая проверяет, является ли строка палиндромом. Без срезов и reversed(), только рекурсия.
2. Напишите функцию make_validator(min_val, max_val), которая возвращает функцию-валидатор. Валидатор принимает число и возвращает True если оно в диапазоне, иначе False.
3. Напишите декоратор @retry(n), который при возникновении любого исключения повторяет вызов функции до n раз. Если все попытки провалились — пробрасывает последнее исключение.
4. Напишите декоратор @deprecated(message), который выводит предупреждение при вызове функции (через warnings.warn) и всё равно выполняет её. Сохраняйте метаданные через functools.wraps.
5. Напишите рекурсивную функцию binary_search(lst, target) (бинарный поиск числа в списке), оберните её декоратором @logger, который логирует каждый вызов с параметрами.
"""

task = "Напишите рекурсивную функцию palindrome(s), которая проверяет, является ли строка палиндромом. Без срезов и reversed(), только рекурсия."
task_visualization(1, task)


def palindrome(s: str) -> bool:
    print(s)
    if len(s) < 2:
        return True
    
    return palindrome(s[1:-1]) if s[0] == s[-1] else False


print(palindrome("StrRtS"))
     

task = "Напишите функцию make_validator(min_val, max_val), которая возвращает функцию-валидатор. Валидатор принимает число и возвращает True если оно в диапазоне, иначе False."
task_visualization(2, task)

def make_validator(min_val: int, max_val: int) -> Callable[[int], bool]:
    def fun_validator(x: int) -> bool:
        nonlocal min_val, max_val

        return True if x > min_val and x < max_val else False
    
    return fun_validator


print(make_validator(1, 3)(7))


task = "Напишите декоратор @retry(n), который при возникновении любого исключения повторяет вызов функции до n раз. Если все попытки провалились — пробрасывает последнее исключение."
task_visualization(3, task)


def retry(n: int) -> Callable:
    def decoretor(func: Callable) -> Callable:
        def inner(*args, **kwargs) -> str:
            last_error = None
            for _ in range(n):
                try:
                    return func(*args, **kwargs)
                except Exception as error:
                    last_error = error

            raise last_error

        return inner
    
    return decoretor

@retry(5)
def get_error():
    return 12 - "2"


get_error()


task = "Напишите декоратор @deprecated(message), который выводит предупреждение при вызове функции (через warnings.warn) и всё равно выполняет её. Сохраняйте метаданные через functools.wraps."
task_visualization(4, task)


def deprecated(message: str) -> Callable:
    def decorator(func) -> Callable:
        @wraps(func)
        def inner(*args, **kwargs):
            warnings.warn(message)
            return func(*args, **kwargs)
        
        return inner
    
    return decorator


warnings.simplefilter("always")


@deprecated("Be carefull !")
def check_deprecated():
    print("FFFFF")


check_deprecated()
check_deprecated()


task = "Напишите рекурсивную функцию binary_search(lst, target) (бинарный поиск числа в списке), " \
"оберните её декоратором @logger, который логирует каждый вызов с параметрами."
task_visualization(5, task)


def logger(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Using {func.__name__} with args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper

@logger
def binary_search(lst: list[int], target: int) -> int | Callable:

    if not lst:
        return -1
    
    mid = len(lst) // 2

    if lst[mid] == target:
        return mid
    
    elif lst[mid] < target:
        result = binary_search(lst[mid + 1:], target)
        return -1 if result == -1 else mid + 1 + result

    else:
        return binary_search(lst[:mid], target)


print(binary_search([1, 2, 3, 4, 5, 6], 3))
