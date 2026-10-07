D = int(input())
M = int(input())

if D > 1:
    D -= 1
else:
    M -= 1
    if M == 0:
        M = 12
        D = 31
    elif M == 2:
        D = 28
    elif M in (4, 6, 9, 11):
        D = 30
    else:
        D = 31

print(D, M)