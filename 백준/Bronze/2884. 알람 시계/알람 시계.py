h, m = map(int,input().split())

if m > 44: # 45분 초과일 때
    print(h, m-45)
elif h > 0 and m < 45: # 1시초과 그리고 45분 미만일 때
    print(h-1, m+15)
else: # 자정 0시일때만 23시
    print(23, m+15)