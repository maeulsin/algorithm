x = int(input())
n = int(input())
result = 0
for _ in range(n):
    a, b = map(int,input().split())
    d = a * b
    result = result + d

if result == x:
    print('Yes')
else:
    print('No')