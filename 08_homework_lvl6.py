# Практическое задание
# 1. В этой игре человек загадывает число, а компьютер пытается его угадать.
# В начале игры человек загадывает число от 1 до 100 в уме или записывает его на листок бумаги.
# Компьютер начинает его отгадывать предлагая игроку варианты чисел. Если компьютер угадал число,
# игрок выбирает “победа”. Если компьютер назвал число меньше загаданного, игрок должен выбрать
# “загаданное число больше”. Если компьютер назвал число больше, игрок должен выбрать “загаданное число меньше”.
# Игра продолжается до тех пор пока компьютер не отгадает число.

maxi = 100
version = int(maxi / 2)
gap = int(version/2)
gap_count = 0
answer = "0"

while True:
    print("        MAXi:", maxi, "version:", version, "gap:", gap)
    answer = input("Is this {}? Answer +, - or =: ".format(version))
    if answer == "=":
        print("Win! Your number was", version)
        break
    elif answer == "+":
        version = int(version + gap)
        if gap == 1:
            print("Win! Your number was", version)
            break
    elif answer == "-":
        version = int(version - gap)
        if gap == 1:
            print("Win! Your number was", version)
            break
    else:
        print('incorrect answer, plz type: "+" or "-" or "="')
        continue
    gap = int(gap/2)
    if gap == 1:
        if gap_count == 0:
            gap = 2
            gap_count += 1
    if gap == 0:
        gap = gap + 1



