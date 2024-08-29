def solution(i, j, k):
    answer = 0
    
    k = str(k)
    
    for c in range(i, j + 1):
        answer += str(c).count(k)
        
    return answer