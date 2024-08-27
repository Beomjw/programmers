def solution(numbers):
    answer = 0
    answer = sorted(numbers)
    a = answer[0] * answer[1]
    b = answer[-1] * answer[-2]
    if a > b:
        return a
    else:
        return b
