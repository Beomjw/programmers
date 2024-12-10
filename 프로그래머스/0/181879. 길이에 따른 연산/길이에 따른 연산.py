def solution(num_list):
    l = len(num_list)
    if l >= 11:
        answer = 0
        for num in num_list:
            answer += num
    else:
        answer = 1
        for num in num_list:
            answer *= num
    return answer