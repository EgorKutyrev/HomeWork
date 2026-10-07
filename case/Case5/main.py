import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    N = int(data[0])
    A = float(data[1])
    B = float(data[2])
    if N == 1:
        print(A + B)
    elif N == 2:
        print(A - B)
    elif N == 3:
        print(A * B)
    elif N == 4:
        print(A / B)

if __name__ == "__main__":
    main()