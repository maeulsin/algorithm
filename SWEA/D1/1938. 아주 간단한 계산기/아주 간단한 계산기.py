a, b = list(map(int,input().split()))
n = a + b
n1 = a - b
n2 = a * b
n3 = a // b

list = [n, n1, n2, n3]
for char in list:
    print(char)