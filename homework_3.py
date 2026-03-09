def visualization(task_number, text):
    print("\n" + "=" * 40)
    print(f"Task {task_number}".center(40))
    print("-" * 40)
    print(text)
    print("=" * 40 + "\n")




task = "привести к целому типу -1.6, 2.99"
visualization(1, task)
a = int(-1.6)
b = int(2.99)
print(a, b)


task = "заменить символ # на символ '/' в строке 'www.my_site.com#about'"
visualization(2, task)
stringa = "www.my_site.com#about"
print(stringa.replace('#', '/'))


task = "Напишите программу, которая добавляет 'ing' к слову 'stroka'."
visualization(3, task)
stringa = "stroka"
result = stringa + "ing"
print(result)


task = "В строке 'Ivanov Ivan' поменяйте местами слова => 'Ivan Ivanov'."
visualization(4, task)
stringa = "Ivan Ivanov"
words = stringa.split()
print(words[1], words[0], sep=" ")


task = "Напишите программу, которая удаляет пробел в начале, в конце строки."
visualization(5, task)
stringa = " IvanIvanov "
print(stringa.strip())


task = "Создайте словарь, связав его с переменной school, и наполните его данными, которые бы отражали" + "\n" + \
"количество учащихся в десяти разных классах (например, 1а, 1б, 2б, 6а, 7в и т.д.)."
visualization(6, task)
school = {
    "class 1a": 1,
    "class 1b": 12,
    "class 1c": 15,
    "class 1f": 122,
    "class 1e": 11,
    }
print(school)


task = "Создайте список и извлеките из него второй элемент."
visualization(7, task)
array = [1, 2, 4]
print(array[1])


task = "Вывести, входит ли строка1 в строку2 (пример: employ и employment)."
visualization(8, task)
main_string = "employment"
search_string = "employ"
if main_string.find(search_string) != -1:
    print(True)
else: 
    print(False)


task = "Вывести нужные символы: \n\nprint(x[?]) #y\n" \
"print(x[?:?:?]) #nesgt"
visualization(9, task)
x = 'My name is Agent Smith'
print(x[1]) #y
print(x[3:16:3]) #nesgt


task = "Есть массив чисел. Известно, что каждое число в этом массиве имеет пару, кроме одного: [1, 5, 2, 9, 2, 9, 1] =>5\n" \
"Напишите программу, которая будет выводить уникальное число."
visualization(10, task)

def find_uniq(array):
    for i in array:
        if array.count(i) == 1:
            print(i)
        else:
            print("No unpaired element")

array = [1, 5, 2, 9, 2, 9, 1]
find_uniq(array)