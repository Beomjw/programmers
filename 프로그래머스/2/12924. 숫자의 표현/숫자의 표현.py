def solution(n):
    answer = 0
    for start in range(1, n + 1):
        sum_val = 0
        for num in range(start, n + 1):
            sum_val += num
            if sum_val == n:
                answer += 1
                break
            elif sum_val > n:
                break
    return answer
