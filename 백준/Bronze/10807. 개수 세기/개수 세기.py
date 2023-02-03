n = int(input())
num = list(map(int,input().split()))
a = int(input())

cnt = 0
for i in num:
    if i == a:
        cnt += 1
        
print(cnt)