from itertools import *

def solution(number):
    answer = 0
    # [-2, 3, 0, 2, -5]
    # -2 2 0
    # -5 3 2
    per = list(combinations(number, 3))
    
    for p in per:
        if sum(p) == 0:
            answer += 1
    return answer