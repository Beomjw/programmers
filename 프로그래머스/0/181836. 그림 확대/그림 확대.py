def solution(picture, k):
    answer = []
    for row in picture:
        resized = ''
        for i in row:
            resized += i * k
        for j in range(k):
            answer.append(resized)
    return answer