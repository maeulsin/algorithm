T = int(input())
for T in range(1, T + 1):
    numbers = list(map(int,input().split()))
    result = 0
    result = max(numbers)
    print(f'#{T} {result}')
