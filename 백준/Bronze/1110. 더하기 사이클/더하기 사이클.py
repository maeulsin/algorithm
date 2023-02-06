n = int(input())
num = n
cnt = 0

while True:
    a = num // 10 #2
    b = num % 10 #6
    c = (a+b) % 10 #8
    num = (b * 10) + c

    cnt = cnt + 1

    if num == n:
        break
print(cnt)