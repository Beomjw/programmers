def solution(arr, queries):
    # arr 
    # [0, 1, 2, 3, 4]
    # queries
    # [[0, 1],[1, 2],[2, 3]]
    
    # [1, 2, 2, 3, 4]
    # [1, 3, 3, 3, 4]
    # [1, 3, 4, 4, 4]
    
    for s, e in queries:
        for i in range(s, e+1):
            arr[i] += 1
    return arr