def solution(arr, k):
    answer = []
    # [0, 1, 1, 2, 2, 3]
    # k = 3
    # [0, 1, 2]
    
    # [0, 1, 1, 1, 1]
    # k = 4
    # [0, 1, -1, -1]

    for i in range(len(arr)): # 0 1 2 3 4 5 
        if arr[i] not in answer:
            answer.append(arr[i])
        if len(answer) == k:
            break
    
    while len(answer) < k: # 0 < 3
        answer.append(-1)
        
    return answer