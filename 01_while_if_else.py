#####################
while True:
    number = int(input("введите число"))
    if number > 0 or number < 10:
        print("верное число", number)
        break
    else:    # elif
        print("неверное число, введите пложительное число меньше 10")
# continue - начинает цикл заново не доходя до конца
# else для while - выполняется если while  стал ложью
# ###### СТРОКИ
name = "Mike Sboev"
sybmol_2 = name[1]  # i
sybmol_last = name[-1]  # v
symbols_middle = name[5:7]  # символы с какой по какой, [:3] = Mike   ,  [-5:]
number = len(name)

##############################
name = "Mike Sboev"
print(len(name))  # len - МЕТОД считающий сколько символов в строке
print(name.find("Sbo"))  # find - ФУНКЦИЯ (пишется через точку), показывает в каком месте начинается подстрока,
# в противном случае выдает -1
if name.find("a") == -1:
    print("такой буквы нет", name.find("a"))
# in (также можно not in ) - позваляет получить булевое значение при поиске, напримере предыдущего:
if "a" in name:
    print("буква есть")
else:
    print("буквы нет")
print(name.split())   # разбивает строку на нассив из строк через пробел, print(name.split(";")) - разделитель будет ;
print(name.isdigit())  # проверяет состоит ли строка только из цифр, булевое значение
print(name.lower())  # upper  - делает все символы верним \ нижним регистром
# форматирование строк
name = "Leo"
age = 30
hello_str = "Привет %s тебе %d  лет" % (name, age)  # s - str , d - digit
print(hello_str)
hello_str = "Привет {} тебе {}  лет".format(name, age)
print(hello_str)
