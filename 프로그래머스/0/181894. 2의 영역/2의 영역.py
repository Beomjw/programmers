def solution(arr):
    answer = []
    result = []
    # [1, 2, 1, 4, 5, 2, 9] # [2, 1, 4, 5, 2]
    
    if 2 not in arr:
        return [-1]
    else:
        for a in range(len(arr)): # 1 2 1 4 5 2 9
            if arr[a] == 2: 
                result.append(a) #첫 번째 2 인덱스 번호 1, 두 번째 2 인덱스 번호 5
    return arr[result[0]:result[-1]+1] 