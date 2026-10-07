import math
n = int(input())
v = float(input())
if n == 1:
    a = v
    c = a * math.sqrt(2)
    h = c / 2
    S = c * h / 2
elif n == 2:
    c = v
    a = c / math.sqrt(2)
    h = c / 2
    S = c * h / 2
elif n == 3:
    h = v
    c = 2 * h
    a = c / math.sqrt(2)
    S = c * h / 2
else:
    S = v
    c = math.sqrt(4 * S)
    h = c / 2
    a = c / math.sqrt(2)
print(a)
print(c)
print(h)
print(S)