def solution(rank, attendance):
    result = []
    answer = 0
    
    # [3, 7, 2, 5, 4, 6, 1]
    # [0, 1, 2, 3, 4, 5, 6]
    # [false, true, true, true, true, false, false]
    # [7, 2, 5, 4] -> [2, 4, 5, 7]
    # idex  = [1, 2, 3, 4] -> [2, 4, 3]
    
    # [6, 1, 5, 2, 3, 4]
    # [0, 1, 2, 3, 4, 5]
    # [true, false, true, false, false, true]
    # [6, 5, 4]
    # [0, 2, 5]
    
    for i, val in enumerate(rank):
        if attendance[i] == True: 
            result.append([rank[i], i]) # [[7, 1], [2, 2], [5, 3], [4, 4]]
            
    result.sort() # [[7, 1], [5, 3], [2, 2], [4, 4]]
    
    answer = (10000 * result[0][1]) + (100 * result[1][1]) + result[2][1]
    
    return answer