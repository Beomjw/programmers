def solution(myString):
    answer = ''
    for s in myString:
        if s < 'l':
            s = 'l'
            answer += s
        else:
            answer += s
    return answer