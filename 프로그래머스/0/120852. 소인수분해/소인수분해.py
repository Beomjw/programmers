def solution(n):
    answer = []
    a = 2
    while n > 1:
        if n % a == 0:
            answer.append(a)
            n //= a
            while n % a == 0:
                n //= a
        a += 1
    return sorted(answer)

