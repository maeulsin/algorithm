for num in range(int(input()), 3 , -1): # 입력 받은 숫자에서 4까지 -1씩 줄어듬
    for n in str(num): # 변수 n이 문자열 num에 속해 반복할 때
        if n != '4' and n != '7': # 만약 n에 문자열 4와 7이 들어있지 않다면
            break # 멈춤
    else: # 아닐 경우 출력
        print(num)
        break