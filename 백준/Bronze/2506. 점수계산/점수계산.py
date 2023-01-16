N = int(input())
test = list(map(int,input().split())) 
sum = 0
answer = 0
for i in range(N):  
    if test[i] == 1:
        answer = answer + 1
    else:
        answer = 0
    sum = sum + answer
print(sum)