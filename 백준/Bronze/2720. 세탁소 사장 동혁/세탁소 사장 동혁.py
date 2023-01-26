T = int(input())
for i in range(1, T + 1):
    C = int(input())
    
    q = C // 25
    C = C - q * 25 
    
    d = C // 10 
    C = C - d * 10

    n = C // 5
    C = C - n * 5

    p = C // 1

    print(q, d, n, p)
