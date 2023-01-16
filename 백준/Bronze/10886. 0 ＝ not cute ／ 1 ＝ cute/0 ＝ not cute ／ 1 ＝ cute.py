N = int(input())
cute = 1
notcute = 0
for i in range(N):
    i = int(input())
    if i == 0:
        notcute = notcute + 1
    else:
        cute = cute + 1
if cute > notcute:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")