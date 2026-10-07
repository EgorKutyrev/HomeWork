D = int(input())
M = int(input())

if (M == 1 and D >= 20) or (M == 2 and D <= 18):
    print("Водолей")
elif (M == 2 and D >= 19) or (M == 3 and D <= 20):
    print("Рыбы")
elif (M == 3 and D >= 21) or (M == 4 and D <= 19):
    print("Овен")
elif (M == 4 and D >= 20) or (M == 5 and D <= 20):
    print("Телец")
elif (M == 5 and D >= 21) or (M == 6 and D <= 21):
    print("Близнецы")
elif (M == 6 and D >= 22) or (M == 7 and D <= 22):
    print("Рак")
elif (M == 7 and D >= 23) or (M == 8 and D <= 22):
    print("Лев")
elif (M == 8 and D >= 23) or (M == 9 and D <= 22):
    print("Дева")
elif (M == 9 and D >= 23) or (M == 10 and D <= 22):
    print("Весы")
elif (M == 10 and D >= 23) or (M == 11 and D <= 22):
    print("Скорпион")
elif (M == 11 and D >= 23) or (M == 12 and D <= 21):
    print("Стрелец")
else:
    print("Козерог")