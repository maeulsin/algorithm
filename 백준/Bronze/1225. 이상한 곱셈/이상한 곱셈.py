a, b = input().split()

list_a = list(a) # ['1', '2', '3'] 문자열 분리
list_b = list(b) # ['4', '5']

sum_a = 0
for i in list_a:
    i = int(i)
    sum_a = sum_a + i

sum_b = 0
for j in list_b:
    j = int(j)
    sum_b = sum_b + j

print(sum_a * sum_b)