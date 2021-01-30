import math
import random  # импортирует все функции, чтобы их ипользовать нужно начинать с random.randint
from random import randint  # импортирует только эту функцию из рандома, зато ей можно использовать без префикра random.

r = 100
print(2*r*math.pi)  # длинна окружности
print(r**2*math.pi)  # площадь окружности
print(math.pow(r, 2) * math.pi)  # площадь окружности, возведение во вторую степень через math.pow(r, 2)
print(math.factorial(9))  # факториал

print(random.randint(0, 100))  # рандомное число

winners = ["alex", "mike", "ivan", "nick", "tod"]
print(random.choice(winners))  # выбрать победителя рандомно
print(random.sample(winners, 3))  # выбрать рандомно 3-х победителей

numbers = [8, 12, -3, 6]
random.shuffle(numbers)  # перемешать значения в листе
print(numbers)

print(abs(-9))  # abs модуль числа

numbers = [8, 12, -3, 6]  # min, max, sum - минимальноеб максимальное и сумма листа
print(max(numbers))
print(min(numbers))
print(sum(numbers))

print(round(10.3465, 2))  # round - округление числа, второе число указывает сколько знакоп после запятой оставить

# enumerate - нумерация списка. Цифра 1 означает с какой цифры начинается нумерация. По дефолту с 0
winners = ["alex", "mike", "ivan"]
for number, winner in enumerate(winners, 1):
    print(number, winner)

##########################################
# функции - СОРТИРОВКА    передаем значение, а потом если нужно - ключ
##########################################

numbers = [5, 9, 1, 6, 3, 7]
print(sorted(numbers))  # сортировка по порядку
print(sorted(numbers, reverse=True))  # обратная сортировка

names = ["Max", "Alex", "Kate"]
print(sorted(names))  # сортировка по алфавиту

cities = [("Moscow", 1000), ("Vegas", 500), ("NYC", 2000)]
print(sorted(cities))  # так сработает сортировка по алфавиту городов
# для сортировки по численности нужно использовать доп функцию которая будет брать кортежи из списка и возвращать второе
# значение каждого кортежа из списка


def by_number(city):  # сюда будут по одному приходить кортежи из списка, которые будет передавать сортировка
    return city[1]  # в данном случае мы будет возвращать 2й пункт кортежа, т.к. нумерация с 0


print(sorted(cities, key=by_number))  # в качестве ключа используем функцию
print("lambda", (sorted(cities, key=lambda city: city[1])))  # тоже самое через лямбду


##########################################
# функции - ФИЛЬТР.  В фильтре передаются сначало фильтр, потом фильтруемое
##########################################
print("FILTERS")
numbers = list(range(10))


def even(num):
    return num % 2 == 0


result = filter(even, numbers)
print(result)  # так как в эту переменную мы сохранили результат фильтрации и это лист то выдаются кракозябры
result = list(result)  # приводим переменную к типу лист и все становится ОК
print(result)

result = filter(lambda num: num > 5, numbers)
print(list(result))


# функции - ФИЛЬТР для текстовых листов
names = ["Max", "Alex", "Kate"]

result = filter(lambda l: len(l) > 3, names)
print(list(result))


##########################################
# функции - MAP.
##########################################
numbers = [5, 9, 1, 6, 3, 7]

print(list(map(lambda x: x**2, numbers)))  # возвести все числа в квадрат

print(list(map(lambda x: str(x), numbers)))  # перевести все цифры в строки
