def solution(numbers, n):
    answer = 0
    s = 0
    for i in range(len(numbers)):
        s += numbers[i]
        if s > n:
            break
    return s
            
