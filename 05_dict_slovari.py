#

dog_1 = {
    "name": "Greed",
    "age": 5,
    "sex": "male"
}

print(dog_1["age"])
print(dog_1)
dog_1["has_house"] = True

del dog_1["sex"]

print(dog_1)

if "has_house" in dog_1:
    print("This dog has house")

print("==============  ЦИКЛЫ  ================")

for key in dog_1.keys():
    print(key, "::", dog_1[key])

for val in dog_1.values():
    print(val)

for item in dog_1.items():  # возвращает КОРТЕЖИб можно использовать индексы чтобы брать нужный элемент  из кортежа
    print(item)

for key, val in dog_1.items():
    print(key, "===", val)


