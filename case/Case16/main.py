n = int(input())
tens = n // 10
ones = n % 10

tens_words = {
    2: "двадцать",
    3: "тридцать",
    4: "сорок",
    5: "пятьдесят",
    6: "шестьдесят"
}

ones_words = {
    0: "",
    1: "один",
    2: "два",
    3: "три",
    4: "четыре",
    5: "пять",
    6: "шесть",
    7: "семь",
    8: "восемь",
    9: "девять"
}

if ones == 1:
    suffix = "год"
elif ones in (2, 3, 4):
    suffix = "года"
else:
    suffix = "лет"

result = tens_words[tens]
if ones != 0:
    result += " " + ones_words[ones]
result += " " + suffix

print(result)