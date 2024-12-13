def solution(arr):
    answer = []
    
    for i in arr: # [5, 1, 4]
        for j in range(i): # 0 1 2 3 4 / 0 / 0 1 2 3
            answer.append(i) # [5, 5, 5, 5, 5, 1, 4, 4, 4, 4]
    
    return answer