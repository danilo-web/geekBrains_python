import random

print(random.randint(5, 15))  # рандомное число в интервале

# вывести нечетные числа
numbers = [1, 3, 5]

print(random.choice(numbers))  # напечатать рандомное число из списка

for number in numbers:
    print(number)

for i in range(1, 11):  # задаем цикл с 10 кратным повторением
    folder_name = f"folder{i}"  # печатаем 10 раз имя папки каждый раз меняя ее номер
    print(folder_name)

num = range(7)  # задаем переменную-массив в котором 7 значений от 0 до 6
print(num)  # покажет что это ренж и в каком диапозоне, т.к. внутри ренжа всегда цифры идут по порядку
print(type(num))
print(list(num))  # напечатает весь лист из ренжа

print(list(range(0, 1000, 50)))  # начало списка, конец списка (не включая это число), шаг)


for number in range(1, 10, 2):
    print(number)

# winners
winners = ["max", "tom", "alex"]

# простой перебор
for winner in winners:
    print(winner)

for i in range(len(winners)):
    print(i+1, ")", winners[i])



