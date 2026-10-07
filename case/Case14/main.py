import math

n = int(input())
v = float(input())

if n == 1:
    a = v
    r1 = a * math.sqrt(3) / 6
    r2 = 2 * r1
    s = a * a * math.sqrt(3) / 4
elif n == 2:
    r1 = v
    a = 6 * r1 / math.sqrt(3)
    r2 = 2 * r1
    s = a * a * math.sqrt(3) / 4
elif n == 3:
    r2 = v
    r1 = r2 / 2
    a = 6 * r1 / math.sqrt(3)
    s = a * a * math.sqrt(3) / 4
else:
    s = v
    a = math.sqrt(4 * s / math.sqrt(3))
    r1 = a * math.sqrt(3) / 6
    r2 = 2 * r1

print(a)
print(r1)
print(r2)
print(s)