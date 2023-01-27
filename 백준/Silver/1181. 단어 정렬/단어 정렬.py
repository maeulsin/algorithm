n = int(input())
stack = []
for _ in range(n):
    stack.append(input())

word = list(set(stack)) 

word2 = [] 
for i in word: 
    word2.append((len(i), i)) 

result = sorted(word2)

for len, voca in result:
    print(voca)