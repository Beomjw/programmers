def solution(start_num, end_num):
    answer = []
    for a in range(end_num, start_num+1):
        answer.append(a)
    answer.sort(reverse=True)
    return answer