import math

n = int(input())
value = float(input())

if n == 1:
    R = value
elif n == 2:
    R = value / 2
elif n == 3:
    R = value / (2 * math.pi)
elif n == 4:
    R = math.sqrt(value / math.pi)

D = 2 * R
L = 2 * math.pi * R
S = math.pi * R * R

print(R)
print(D)
print(L)
print(S)