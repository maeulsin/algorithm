T = int(input())
for test_case in range(1, T + 1):
    numbers = list(map(int,input().split()))
    avg_value=sum(numbers)/len(numbers)
    avg_value=round(avg_value)
    print("#{} {}".format(test_case,avg_value))
