def solution(n):
    answer = [[] for i in range(n)] # n이 3일때 [[], [], []] 생성
    for i in range(n): # 0, 1, 2
        for j in range(n): # 0, 1, 2
            if i == j: # [0,0], [1,1], [2,2] 일때 리스트에 1추가 아니면 0 추가
                answer[i].append(1)
            else:
                answer[i].append(0)
    return answer