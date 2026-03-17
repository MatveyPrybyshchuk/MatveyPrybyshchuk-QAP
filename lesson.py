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


def is_palindrome_1(word: str) -> bool:
    word = word.lower().strip()
    return word == word[::-1]

def is_palindrome_2(word: str) -> bool:
    word = word.lower().strip()
    for i in range(0, len(word) // 2):
        if word[i] != word[-i - 1]:
            return False
    return True


print(is_palindrome_1("Pap "))
print(is_palindrome_2("Pap"))
