def solution(my_string, m, c):
    answer = ''
    result = []
    # programmers
    # m = 1, c = 1
    # 한줄에 1글자씩 가로로 작성 -> programmers
    # 왼쪽부터 세로로 1번째 열에 적힌 글자들
    
    # ihrhbakrfpndopljhygc
    # m = 4, c = 2
    # 한줄에 4글자씩 가로로 작성
    # ihrh
    # bakr
    # fpnd
    # oplj
    # hygc
    # 왼쪽부터 세로로 2번째 열에 적인 글자 -> happy
    l = len(my_string) # l = 20
    for i in range(l//m): # 4글자씩 0 ~ 4 / 4 ~ 8 / 8 ~ 12 / 12 ~ 16 / 16 ~ 20   
        result.append(my_string[i*m:(i+1)*m])
    
    for j in result: # 0 1 2 3 4
        answer += j[c-1]
        
    return answer