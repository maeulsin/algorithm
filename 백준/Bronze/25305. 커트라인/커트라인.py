n, k = map(int,input().split())
score = list(map(int,input().split()))
a = sorted(score)
b = a[-k::]
print(min(b))