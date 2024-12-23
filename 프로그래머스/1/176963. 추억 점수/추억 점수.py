def solution(name, yearning, photo):
    answer = []
    
    for p in photo:
        year = 0
        for i in range(len(name)):
            if name[i] in p:
                year += yearning[i]
        answer.append(year)
    return answer