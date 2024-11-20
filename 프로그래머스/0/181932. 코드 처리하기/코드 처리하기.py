def solution(code):
    answer = ''
    # mode = 0
    # code[idx] idx가 짝수일때만 ret 맨 뒤에 code[idx] 추가
    # mode = 1
    # code[idx] idx가 홀수일때만 ret 맨 뒤에 code[idx] 추가
    
    # mode = 0 으로 시작
    
    # abc1abc1abc
    # a c  b  a c
    mode = 0
    for i in range(len(code)):
        if code[i] == '1':
            mode = 1 - mode
        else:    
            if mode == 0 and i % 2 == 0:
                    answer += code[i]
            elif mode == 1 and i % 2 != 0:
                    answer += code[i]
    
    if answer is '':
        return "EMPTY"
    else:
        return answer