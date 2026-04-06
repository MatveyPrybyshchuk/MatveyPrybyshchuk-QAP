from prints.prints_homework import task_visualization


text_1 = "Создай класс Library с атрибутом класса books = [] и методами add_book(title), remove_book(title) и show_books(). Продемонстрируй, что список книг общий для всех объектов класса."
text_2 = "Создай иерархию: базовый класс Employee с атрибутами name и salary, методом get_info(). Дочерние классы Manager (добавляет department) и Developer (добавляет language). Каждый переопределяет get_info()."
text_3 = "Реализуй класс Stack (стек) с протектед атрибутом _items = [] и методами push(item), pop(), peek() (посмотреть верхний элемент), is_empty() и size()."
text_4 = "Создай класс Vehicle с методом move(), выводящим 'Moving...'. Создай дочерние классы Car, Boat и Plane, каждый переопределяет move() по-своему. Напиши функцию start_journey(vehicle), которая вызывает move() у любого переданного транспорта - продемонстрируй полиморфизм."
text_5 = "Создай класс Student с атрибутами name и grades (список оценок). Добавь методы add_grade(grade), average() (средняя оценка), highest() и lowest(). Защити grades через одиночное подчёркивание."


# ---------------------------------------
task_visualization(1, text_1)

class Library:
    books = []

    @classmethod
    def add_book(self, title: str) -> None:
        if title not in self.books:
            self.books.append(title)

    @classmethod
    def remove_book(self, title: str) -> None:
        if title in self.books:
            self.books.remove(title)

    @classmethod
    def show_books(self) -> None:
        print(self.books)

lib_1 = Library()
lib_2 = Library()
lib_3 = Library()

lib_1.add_book("Book_1")
lib_2.add_book("Book_2")
lib_3.remove_book("Book_1")

lib_1.show_books()


# ---------------------------------------
task_visualization(2, text_2)

class Employee:
    def __init__(self, name: str, salary: int) -> None:
        self.name = name
        self.salary = salary

    def get_info(self) -> str:
        return f"Name: {self.name} Salary: {self.salary}"


class Manager(Employee):
    def __init__(self, name: str, salary: int, department: str) -> None:
        super().__init__(name, salary)
        self.department = department

    def get_info(self) -> str:
        return f"Name: {self.name} Salary: {self.salary} Department: {self.department}"

class Developer(Employee):
    def __init__(self, name: str, salary: int, language: str):
        super().__init__(name, salary)
        self.language = language
    
    def get_info(self) -> str:
        return f"Name: {self.name} Salary: {self.salary} Language: {self.language}"
    

emp = Employee("Name_1", 15)
mng = Manager("Name_2", 20, "Depatrment")
drv = Developer("Name_3", 30, "Java")

print(emp.get_info())
print(mng.get_info())
print(drv.get_info())


# ---------------------------------------
task_visualization(3, text_3)

class Stack:
    _items = []
    
    def push(self, item):
        self._items.append(item)

    def pop(self):
        self._items.pop()
        
    def peek(self):
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def size(self) -> int:
        return len(self._items)
    
st_1 = Stack()

print(st_1.is_empty())
st_1.push(10)
print(st_1.is_empty())
print(st_1.peek())
print(st_1.size())
st_1.pop()
print(st_1.size())


# ---------------------------------------
task_visualization(4, text_4)

class Vehicle():
    def move(self):
        print("Moving")

class Car(Vehicle):
    def move(self):
        print("Car is moving")

class Boat(Vehicle):
    def move(self):
        print("Boat is moving")

class Plane(Vehicle):
    def move(self):
        print("Plane is moving")


vehicle = Vehicle()
car = Car()
boat = Boat()
plane = Plane()

def start_journey(vehicle):
    vehicle.move()

start_journey(vehicle)
start_journey(car)
start_journey(boat)
start_journey(plane)


# ---------------------------------------
task_visualization(5, text_5)

class Student():

    def __init__(self, name: str, grades: list):
        self.name = name
        self._grades = grades


    def add_grade(self, grade: int):
        self._grades.append(grade)

    def average(self) -> float:
        return sum(self._grades) / len(self._grades)
    
    def highest(self):
        return max(self._grades)

    def lowest(self):
        return min(self._grades)


st_1 = Student("Name", [])
st_1.add_grade(1)
st_1.add_grade(10)

print(st_1.average())
print(st_1.highest())
print(st_1.lowest())
