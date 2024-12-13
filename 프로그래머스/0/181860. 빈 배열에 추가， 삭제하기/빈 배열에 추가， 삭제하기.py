def solution(arr, flag):
    answer = []
    # [3, 2, 4, 1, 3]
    # [true, false, true, false, false]	
    # [3, 3, 3, 3, 3, 3]
    # [3, 3, 3, 3]
    # [3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4]
    # [3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4]
    # [3, 3, 3, 3, 4, 4, 4, 4]
    
    for i in range(len(arr)):
        if flag[i]:
            for j in range(arr[i]*2): # 0 1 2 3 4 5
                answer.append(arr[i])
        else:
            answer = answer[:-arr[i]]
    return answer