def solution(numbers):
    answer = 0
    n = sorted(i for i in numbers)
    answer = n[-1] * n[-2]
    return answer