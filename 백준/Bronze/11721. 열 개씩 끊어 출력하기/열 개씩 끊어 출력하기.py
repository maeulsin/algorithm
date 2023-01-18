word = input()
a = len(word)
for i in range(0, a, 10):
    result = i + 10
    print(word[i:result])