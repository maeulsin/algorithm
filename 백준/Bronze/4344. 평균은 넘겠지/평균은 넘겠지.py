
a = int(input())
for _ in range(a):
    num = list(map(int,input().split()))
    cnt = 0
    for i in num[1:]:
        avg = sum(num[1:])/num[0]
        if i > avg:
            cnt += 1
    rate = cnt/num[0] * 100
    print(f'{rate:.3f}%')