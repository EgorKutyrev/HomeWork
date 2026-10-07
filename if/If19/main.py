a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a != b and a != c and a != d:
    print(1)
elif b != a and b != c and b != d:
    print(2)
elif c != a and c != b and c != d:
    print(3)
else:
    print(4)