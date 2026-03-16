"""
Попроси пользователя ввести 3 числа через пробел (одной строкой),
преобразуй их в список целых чисел с помощью map и выведи их сумму.
"""

# numbers = input("Insert input a, b, c using space:")

# list_num = numbers.split(sep=" ")

# int_nums = map(int, list_num)
# result = sum(int_nums)

# print(result)

"""
Напиши функцию is_palindrome(word), 
которая возвращает True, если слово является палиндромом.
"""


def is_palindrome(word: str) -> str:
    word = word.lower().strip()
    return word == word[::-1]


print(is_palindrome("Pap "))
