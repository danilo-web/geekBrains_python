girls = ("Ksu", "Lara", "Olga")  # в круглых скобках - кортеж (tuple) - не изменяемый списокб используют для безопасн

friends = ["Leo", "Tim", "Mike", "Tom", "Fred"]
print("второй друг", friends[1])
print("первый друг с конца", friends[-1])
print("друзья 2-4", friends[1:4])


# len(friends) -  длинна списка (сколько в нем элементов)
# friends.append("Ron") - добавление нового элемента
# friends.pop() - удаляем последний элемент и вoзвращаем его
# friends.clear() - очищаем  весь список
# friends.remove("Ron") - удаляем обьект
# del friends[0] - удаление обьекта по индексу

# friends.reverse()- перевернуть список задом наперед
# sorted(friends) - сортирует список

#     in
if "Leo" in friends:
    print("Leo наш друг")


# программа Винерз - награждаем победителей
names = []
count = int(input("сколько участников: "))

while count > 0:
    names.append(input("Введите имя учистника №{}: ".format(count)))
    count -= 1

winners = sorted(names)[:3]
print("Победители:", winners)

# задачка по джаве
numbers = [36578, 694729, 6968476, 6967378, 696745, 98478]

for num in numbers:
    new_num = num % 100  # оставляет посление 2 цифры
    print(new_num)
    # new_num = int(str(num)[-2:])  # перевод в стр чтобы по модулю выбрать последние 2 символа и перевод обратно в int
    # if new_num == 78:
    #     print(num)

# ++++++++++++++ list из str в инт +++++++++++++

list_a = ["3", "4"]
list_a = list(map(int, list_a))
print(list_a)

numbers = ["3", "4"]
print(list(map(lambda x: int(x), numbers)))  # перевести все цифры в строки