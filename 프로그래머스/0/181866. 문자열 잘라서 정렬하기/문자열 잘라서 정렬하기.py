def solution(myString):
    answer = myString.split('x')
    result = []
    for a in answer:
        if a:
            result.append(a)
    result.sort()
    return result