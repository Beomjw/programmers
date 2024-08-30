def solution(score):
    answer = []

    for s in score:
        answer.append((s[0] + s[1]) / 2)
    
    sorted_answer = sorted(answer, reverse=True)
    
    result = []
    
    for a in answer:
        result.append(sorted_answer.index(a) + 1)
    
    return result