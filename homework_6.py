from prints.prints_homework import task_visualization
import os
import datetime
from typing import Callable


task = "Напиши функцию copy_file(source: str, destination: str) -> bool " \
"которая читает содержимое файла source и записывает его в destination. " \
"Возвращает True если успешно. Проверь что файл-копия создался."
task_visualization(1, task)

def copy_file(source: str, destination: str) -> bool:
    try:
        with open(source, mode = "r") as src:
            with open(destination, mode = "w") as dst:
                for line in src:
                    dst.write(line)

        return os.path.exists(destination)
    
    except Exception:
        return False

print(copy_file("source.txt", "destination.txt"))



task = "Создай файл grades.txt где каждая строка содержит имя студента и его оценку через запятую:" \
"Анна,85" \
"Иван,72" \
"Петр,91" \
"Напиши код который читает файл и добавляет в конец каждой строки статус: " \
"'отлично' если оценка >= 90, 'хорошо' если >= 75, иначе 'удовлетворительно'. " \
"Сохрани результат в новый файл grades_with_status.txt."
task_visualization(2, task)

def check_grades():
    with (open("grades.txt", mode = "r", encoding="utf-8") as src,
          open('grades_with_status.txt', mode = "w", encoding="utf-8") as dst
    ):
        for line in src:
            line = line.strip()
            _, grade = line.split(",")
            if int(grade) >= 90:
                dst.write(f"{line}: отлично\n")
            elif int(grade) >= 75:
                dst.write(f"{line}: хорошо\n")
            else:
                dst.write(f"{line}\n")

check_grades()



task = "Напиши функцию age_calculator(birth_date_str: str) -> int которая принимает дату рождения в формате 'dd/mm/yyyy' (input)  и возвращает полных лет. "
task_visualization(3, task)


def age_calculator(birth_date_str: str) -> int:
    day, month, year = map(int, birth_date_str.split("/"))

    today = datetime.datetime.now()
    age = today.year - year

    if (today.month, today.day) < (month, day):
        age -= 1

    return age

print(age_calculator('05/05/2000'))



task = "Напиши модуль file_utils.py с тремя полностью аннотированными функциями:" \
"def read_lines(filename): ..." \
"def write_lines(filename, lines): ... " \
"def count_words(filename): ... # count_words считает сколько раз каждое слово встречается в файле и возвращает словарь. " \
"В main.py импортируй и протестируй все три."
task_visualization(4, task)









task = "5. Напиши функцию password_checker(correct_password) которая возвращает вложенную функцию check(password). " \
"Вложенная принимает пароль и возвращает True если совпадает, иначе False. " \
"Внешняя переменная с паролем не должна быть доступна снаружи"
task_visualization(5, task)


def password_checker(correct_password: str) -> Callable:
    def check(password: str) -> bool:
        return password == correct_password
    return check

print(password_checker("password")("passwordDFD"))
