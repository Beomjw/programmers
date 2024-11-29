def solution(a, d, included):
    answer = 0
    arr = [a]
    # 등차수열의 일반항 : a + (n-1)d
    
    for i in range(1, len(included)):
        arr.append(a + i*d)
    
    for i in range(len(included)):
        if included[i] == 1:
            answer += arr[i]
        
    return answer