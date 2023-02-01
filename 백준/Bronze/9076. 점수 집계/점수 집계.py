t = int(input())

for i in range (t):
    n = list(map(int,input().split()))
    n.remove(max(n))
    n.remove(min(n))
    if max(n) - min(n) >= 4:
        print("KIN")
    else:
        print(sum(n)) 