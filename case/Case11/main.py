D = int(input())
M = int(input())

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

D += 1
if D > days_in_month[M - 1]:
    D = 1
    M += 1
    if M > 12:
        M = 1

print(D)
print(M)