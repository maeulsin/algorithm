n_list = []
average = 0 
for _ in range(5):
    n = int(input())
    n_list.append(n)
    
n_list.sort()  
average = sum(n_list) // len(n_list)
print(average)    
print(n_list[2])