input("как вас зовут? ")
# типы переменных int \ float  \ bool  \  None - пустой тип  \  str
name = "Mike"
print(type(name))
bul_type = True
print(type(bul_type))
date = "22"
print(type(date))
date = int(date)
print(type(date))
new_date = str(date) + " число"
print(type(new_date))
# #######################
# print + sep=   - разделитель,   end=   -  замена окончания,  \n - с новой строки
print("text", "is", "here", sep="\n")
print("w", end=" ")
print("t", end="/")
print("f",  end=" ")
############################
new_name = input("введите имя")
new_age = int(input("ваш возраст"))
#############################
# ПРИ ДЕЛЕНИИ ВСЕГДА ПОЛУЧАЕТСЯ float
print(5 // 2)   # целая часть от деления
print(5 % 2)  # остаток от деления
print(2 ** 3)  # возведение в степень
#   ==   !=    >=   <=   >   <    and   or    not    num += 1
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
# in (также можно not in ) - позволяет получить булевое значение при поиске, напримере предыдущего:
if "a" in name:
    print("буква есть")
else:
    print("буквы нет")
print(name.split())   # разбивает строку на нассив из строк через пробел, если слова в строке разделены например : то
# print(name.split(".")) - поможет айти места разделения. например для даты 01.01.2021 - разделитель "."
print(name.isdigit())  # проверяет состоит ли строка только из цифр, булевое значение
print(name.lower())  # upper  - делает все символы верним \ нижним регистром


# форматирование строк
name = "Leo"
age = 30

hello_str = "Привет %s тебе %d  лет" % (name, age)  # s - str , d - digit
print(hello_str)

hello_str = "Привет {} тебе {}  лет".format(name, age)
print(hello_str)

result = f'{name} {age}'
print(result)
