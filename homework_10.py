from prints.prints_homework import task_visualization
from dataclasses import dataclass
import math


text_1 = "Создай класс Circle с protected атрибутом _radius. Добавь @property для radius (с проверкой: радиус > 0), и вычисляемые свойства area и perimeter через @property - они должны пересчитываться автоматически при изменении радиуса."
text_2 = "Создай класс Vector с атрибутами x и y. Реализуй магические методы __add__ (сложение двух векторов), __str__ (вывод в формате 'Vector(x, y)'), и __eq__ (сравнение). Проверь: Vector(1, 2) + Vector(3, 4) должен давать Vector(4, 6)."
text_3 = "Создай класс Temperature с @property для celsius, fahrenheit и kelvin. При установке значения через любое свойство должны автоматически пересчитываться остальные. Хранить следует только одно внутреннее значение."
text_4 = "Используй @dataclass для создания класса Point с полями x: float и y: float. Добавь метод distance_to(other: Point) - расстояние до другой точки. Затем создай дочерний @dataclass класс Point3D, добавив поле z: float, и переопредели distance_to."
text_5 = "Создай класс-итератор Countdown, который при итерации возвращает числа от start до 0. Реализуй __iter__ и __next__ (при исчерпании бросай StopIteration). Проверь в цикле for и через list()."


# ---------------------------------------
task_visualization(1, text_1)

class Circle():
    
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, radius):
        if radius > 0:
            self._radius = radius
        else:
            raise ValueError("Радиус должен быть больше 0")

    @property
    def area(self):
        return self._radius**2 * 3.14
    
    @property
    def perimeter(self):
        return 2 * 3.14 * self._radius
    
cicle = Circle(5)
print(cicle.area)
print(cicle.perimeter)
    

# ---------------------------------------
task_visualization(2, text_2)

class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other) -> tuple:
        return self.x + other.x, self.y + other.y
    

    def __str__(self) -> str:
        return f"Vector({self.x}, {self.y})"
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    
vec_1 = Vector(1, 2)
vec_2 = Vector(3, 4)
print(vec_1 + vec_2)
print(vec_1)
print(vec_1 == vec_2)


# ---------------------------------------
task_visualization(3, text_3)

class Temperature():

    def __init__(self, kelvin = 0):
        self.kelvin = kelvin
    
    @property
    def kelvin(self):
        return self._kelvin

    @kelvin.setter
    def kelvin(self, kelvin):
        if kelvin < 0:
            raise ValueError("Температура не может быть ниже абсолютного нуля (0 K)")
        self._kelvin = kelvin

    @property
    def celsius(self):
        return self.kelvin - 273.15
    
    @celsius.setter
    def celsius(self, celsius):
        if celsius < -273.15:
            raise ValueError("Температура не может быть ниже абсолютного нуля (-273.15 C)")
        self.kelvin = celsius + 273.15
            
    @property
    def fahrenheit(self):
        return (self.kelvin - 273.15) * 1.8 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, fahrenheit):
        if fahrenheit < -459.67:
            raise ValueError("Температура не может быть ниже абсолютного нуля (-459.67 F)")
        self.kelvin = (fahrenheit - 32) / 1.8 + 273.15
    

temperature = Temperature()
temperature.celsius = 20
print(temperature.celsius)
print(temperature.kelvin)
print(temperature.fahrenheit)


# ---------------------------------------
task_visualization(4, text_4)

@dataclass
class Point():
    x: float
    y: float
    
    def distance_to(self, other: 'Point') -> float:
        dif_x = self.x - other.x
        dif_y = self.y - other.y
        return math.sqrt(dif_x**2 + dif_y**2)


@dataclass
class Point3D(Point):
    z: float

    def distance_to(self, other: 'Point') -> float:
        dif_x = self.x - other.x
        dif_y = self.y - other.y
        dif_z = self.z - other.z
        return math.sqrt(dif_x**2 + dif_y**2 + dif_z**2)


pnt_1 = Point(2, 3.5)
pnt_2 = Point(5.5, 5)

print(pnt_1.distance_to(pnt_2))

pnt_3D_1 = Point3D(2, 3.5, 1)
pnt_3D_2 = Point3D(5.5, 5, 2)

print(pnt_3D_1.distance_to(pnt_3D_2))


# ---------------------------------------
task_visualization(5, text_5)


class Countdown():
    
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current == 0:
            raise StopIteration
        temp = self.current
        self.current -= 1
        return temp
        
for number in Countdown(5):
    print(number)

print(list(Countdown(5)))
