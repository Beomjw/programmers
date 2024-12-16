def solution(order):
    answer = 0
    # 아메리카노 4500
    # 카페 라테 5000
    for o in order:
        if 'americano' in o:
            answer += 4500
        elif 'cafelatte' in o:
            answer += 5000
        elif o == 'anything':
            answer += 4500
    return answer