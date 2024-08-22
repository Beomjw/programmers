def solution(n, k):
    answer = 0
    if n >= 10:
        a = n // 10
    else:
        a = 0
    return 12000*n + 2000*k - 2000*a