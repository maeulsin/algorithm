a = []
for _ in range(10):
    n = int(input())
    a.append(n)
print(int(sum(a) / 10)) # 평균

b = list(set(a)) # [40, 10, 50, 20, 60, 30] a에 있는 중복된 값 제거
c = []
for i in range(len(b)): # len(b) = 6 / b의 길이 만큼 반복
    c.append(a.count(b[i])) # c에 a에서 중복된 값들의 수를 추가 c = [2, 1, 1, 1, 2, 3] 
    #[40:2번, 10:1번, 50:1번, 20:1번, 60:2번, 30:3번] /b[i] = 40 10 50 20 60 30
print(b[c.index(max(c))]) # 최빈수 