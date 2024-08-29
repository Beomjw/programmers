def solution(sides):
    count = 0
    s = sorted(sides)
    min = s[0]
    max = s[1]
    
    count = max - (max - min)
    count += (min + max) - max - 1

    return count
