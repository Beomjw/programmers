from itertools import combinations

def solution(numbers):
    pairs = combinations(numbers, 2)
    
    sums = {sum(pair) for pair in pairs}
    
    return sorted(sums)