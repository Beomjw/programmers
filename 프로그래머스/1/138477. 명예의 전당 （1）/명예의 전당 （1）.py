def solution(k, score):
    answer = []
    fame = []
    # k = 3
    # [10, 100, 20, 150, 1,  100, 200]
    #  10  100 100  150  150 150  200
    #       10  20  100  100 100  150
    #           10   20   20 100  100
    #  10   10  10   20   20 100  100
    
    for i in range(len(score)): # k = 3 0 1 2
        fame.append(score[i])
        fame.sort(reverse=True)
        
        if len(fame) > k:
            fame.pop()
        
        answer.append(fame[-1])
        
    return answer