from prints.prints_homework import task_visualization


task = "Дано целое число. Если оно является положительным, то прибавить к нему 1; " \
"в противном случае не изменять его. Вывести полученное число"
task_visualization(1, task)

num = int(input("Insert num for calculation: "))
print(num + 1 if num % 2 == 0 else num )



task = "Даны три целых числа. Найти количество положительных чисел в исходном наборе."
task_visualization(2, task)

nums = input("Insert 3 num in a row using space: ")
nums_arr = nums.split()

result = 0
for i in nums_arr:
    if int(i) % 2 == 0:
        result += 1

print(result)


task = "Дан номер года (положительное целое число). Определить количество дней " \
"в этом году, учитывая, что обычный год насчитывает 365 дней, а високосный — 366 дней. " \
"Високосным считается год, делящийся на 4, за исключением тех годов, которые" \
"делятся на 100 и не делятся на 400 (например, годы 300, 1300 и 1900 не являются" \
"високосными, а 1200 и 2000 являются)."
task_visualization(3, task)

year = int(input("Insert year for calculations: "))

result = 365
if year % 4 == 0 and not (year % 400 != 0 and year % 100 == 0):
    result += 1

print(result)



task = "Найти сумму всех натуральных чисел в от A до B"
task_visualization(4, task)

inputs = input("Insert num A and B using space: ")
inputs_arr = list(map(int, inputs.split()))

result = 0
for i in range(inputs_arr[0], inputs_arr[1]+1):
    result += i

print(result)



task = "Найти произведение положительных, сумму и количество отрицательных" \
"из 10 введенных целых значений. (Функция ввода с клавиатуры - input())"
task_visualization(5, task)

inputs = input("Insert 10 nums using space: ")
inputs_arr = list(map(int, inputs.split()))

multipl, neg_sum, neg_count = 1, 0, 0

for i in inputs_arr:
    if i > 0: 
        multipl *= i
    elif i < 0: 
        neg_count += 1
        neg_sum += i


print(f"Произведение положительных: {multipl if multipl != 1 else 0}, "
      f"Сумма отрицательных: {neg_sum}, "
      f"Количество отрицательных: {neg_count}")



task = "Дано число N. Найти произведение всех чисел от 0 до N."
task_visualization(6, task)

num = int(input("Insert num N: "))

result = 1
for i in range (1, num):
    result *= i

print(result)



task = "Поле засеяли цветами двух сортов на площади S1 и S2. Каждый год "\
" площадь цветов первого сорта увеличивается вдвое, а площадь второго сорта "\
"увеличивается втрое. Через сколько лет площадь первых сортов будет "\
"составлять меньше 10% от площади вторых сортов."
task_visualization(7, task)

area_S1, area_S2 = map(int, input("Insert S1 and S2 using space: ").split())

if area_S1 <= 0.1 * area_S2:
    print(0)
else:
    counter = 0
    while area_S1 > 0.1 * area_S2:
        area_S1 *= 2
        area_S2 *= 3
        counter += 1
    print(counter)



task = "Напишите алгоритм для определения, является ли число n счастливым. " \
"Счастливое число определяется следующим процессом: " \
"Начиная с любого положительного целого числа, замените число суммой квадратов его цифр. " \
"Повторяйте процесс до тех пор, пока число не станет равным 1 (на этом значении оно и останется), " \
"или пока не замкнется в бесконечном цикле, не включающем 1. Числа, для которых этот процесс заканчивается на 1, " \
"являются счастливыми. Верните true, если n — счастливое число, и false, если нет."
task_visualization(8, task)

num = int(input("Insert num: "))

def isLucky(num):
    history = set()
    while num != 1:
        if num in history:
            return False
        history.add(num)

        num = sum(int(i)**2 for i in str(num))
    return True
       
print (isLucky(num))


