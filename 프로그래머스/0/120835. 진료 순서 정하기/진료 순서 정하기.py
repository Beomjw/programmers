def solution(emergency):
    answer = []
    sorted_emergency = sorted(emergency, reverse=True)
    
    for i in emergency:
        rank = sorted_emergency.index(i) + 1
        answer.append(rank)
    
    return answer
