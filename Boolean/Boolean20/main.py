n = int(input())
a = n // 100
b = (n // 10) % 10
c = n % 10
print(a != b and b != c and a != c)