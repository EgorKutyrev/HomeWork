A = float(input())
B = float(input())
C = float(input())
if abs(B - A) < abs(C - A):
    print(B, abs(B - A))
else:
    print(C, abs(C - A))