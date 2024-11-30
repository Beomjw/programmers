def solution(numLog):
    answer = ''
    # 0 -> 1 이면 w
    # 0 -> 10 이면 d
    # 0 -> -1 이면 s
    
    # 1 -> 0 이면 s
    # 10 -> 0 이면 a
    # -1 -> -2 이면 s
    
    for i in range(1, len(numLog)):
        if (numLog[i] - numLog[i-1]) == 1:
            answer += 'w'
        elif (numLog[i] - numLog[i-1]) == -1:
            answer += 's'
        elif (numLog[i] - numLog[i-1]) == 10:
            answer += 'd'
        elif (numLog[i] - numLog[i-1]) == -10:
            answer += 'a'
              
    return answer