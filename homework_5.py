from prints.prints_homework import task_visualization


task = "Напиши код который выведет таблицу умножения до 10 на N (введенное с клавиатуры) в таком формате"\
" 3 | 6 | 9 | 12 | 15 | 18 | 21 | 24 | 27"
task_visualization(1, task)

num = int(input("Insert num: "))

result = " | ".join(str(num * i) for i in range(1, 11))
print(result)



task = "Попроси пользователя ввести имя и возраст. Выведи фразу: «Через 10 лет тебе будет <X> лет, <ИМЯ>!»"
task_visualization(2, task)

num = input("Insert your name and your age using space: ")
num_arr = num.split()

name = num_arr[1] if num_arr[0].isdigit() else num_arr[0]
age = num_arr[0] if num_arr[0].isdigit() else num_arr[1]

print(f"Через 10 лет тебе будет {int(age) + 10} лет, {name.upper()}!")



task = "Даны два списка цен в долларах и курс валюты. Используй map чтобы перевести все цены в рубли. " \
"Затем используй zip чтобы создать словарь '{'товар: цена_в_рублях'}':"
task_visualization(3, task)

items = ['хлеб', 'молоко', 'кофе']
prices_usd = [1.5, 2.0, 8.0]
rate = 3.2

def usd_to_byn(price: int) -> int:
    return price * rate

prices_byn = list(map(usd_to_byn, prices_usd))

result = dict(zip(items, prices_byn))
print(result)



task = "Напиши функцию fizzbuzz(n) которая принимает число и возвращает строку: 'Fizz' если делится на 3, " \
"'Buzz' если делится на 5, 'FizzBuzz' если делится на оба, иначе само число в виде строки. " \
"Вызови её для чисел от 1 до 20 через map."
task_visualization(4, task)

def fizzbuzz(n: int) -> str:
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)

print(list(map(fizzbuzz, range(1, 21))))


task = "Напиши функцию *args с именем my_stats которая принимает любое количество чисел " \
"и возвращает сразу три значения — минимум, максимум и среднее. "
task_visualization(5, task)

def my_stats(*args: int) -> tuple[int, int, float]:
    return min(args), max(args), sum(args) / len(args)

print(my_stats(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


task = "Напиши функцию build_profile(**kwargs) которая принимает любые именованные аргументы " \
"и возвращает словарь с этими данными плюс автоматически добавляет ключ 'registered': True. " \
"Добавь к функции docstring."
task_visualization(6, task)

def build_profile(**kwargs: int) -> tuple[int, int, float]:
    """
    Fun build_profile is used to create a new dict with existing kargs + aditional key'registered' wit value True.
    """
    return {**kwargs, 'registered': True}

