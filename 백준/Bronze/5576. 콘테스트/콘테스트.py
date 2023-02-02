w = []
k = []

for _ in range(10):
    w.append(int(input()))

for _ in range(10):
    k.append(int(input()))

a = sorted(w) 
b = sorted(k) 

print(sum(a[-3::]), sum(b[-3::]))