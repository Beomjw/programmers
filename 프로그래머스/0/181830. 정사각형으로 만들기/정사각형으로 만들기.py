def solution(arr):
    n = len(arr) # 4
    m = len(arr[0]) # 3
    
    # [[572, 22, 37], 
    # [287, 726, 384], 
    # [85, 137, 292], 
    # [487, 13, 876]]
    
    if n > m: # 4 > 3 
        for i in range(n): # 0 1 2 3
            for j in range(n - m): # 4 - 3 = 1
                arr[i].append(0)
    # [[57, 192, 534, 2], 
    # [9, 345, 192, 999]]
    # m = 4
    # n = 2
    else: # 4 > 2
        for i in range(m - n): # 4 - 2 = 2
            arr.append([0]*m)
    return arr