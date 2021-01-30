def hello(day_time, friend):
    return "Доброе " + day_time + ", " + friend


print(hello("утро", "Вася"))


def greeting(say, *args):  # можно добавлять сколько угодно переменных. В итоге получаем кортеж
    print(say, args)


greeting("Hi", "Leo", "Max", "Tim")


def get_person(**kwargs):  # получаем словарь ключ=значение
    for a, b in kwargs.items():
        print(a, ":", b)


get_person(name="Mike", age=2, car="volvo")


def car(brand="honda", speed=100):
    print(brand, speed)


car("lada")
