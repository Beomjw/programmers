def solution(food):
    answer = ''
    # [1, 3, 4, 6] 0번 음식 한 개, 1번 음식 3개, 2번 음식 4개, 3번 음식 6개
    # 2로 나눔
    # 0은 가운데에 놓고,
    # 1번은 1개씩 
    # 2번은 2개씩
    # 3번은 3개씩
    # "1223330333221"
    
    # [1, 7, 1, 2] 0번 음식 한 개, 1번 음식 7개, 2번 음식 1개, 3번 음식 2개
    # 2로 나눔
    # 0은 가운데에 놓고,
    # 1번은 3개씩
    # 2번은 못쓰고
    # 3번은 1개씩
    # "111303111"
    n = []
    for i in range(1, len(food)): # 0번은 물이므로 패스 1번부터 시작
        if food[i] > 1:
            n.append(food[i] // 2) # n = [3,0,1]
        else:
            n.append(0)
    
    for j in range(len(n)):
        if n[j] != 0:
            answer += str(j+1) * n[j]
    
    answer += '0'
    
    answer += ''.join(reversed(answer[:-1]))
    
    return answer