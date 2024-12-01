# x이 짝수면 2로 나눈다.
# x이 홀수일 때는 3 * x + 1로 바꾸는 계산
def solution(n):
    answer = []
    answer.append(n)
    while n != 1:
        if n % 2 == 0:
            n /= 2
            answer.append(n)
        else:
            n = 3 * n + 1
            answer.append(n)
    return answer