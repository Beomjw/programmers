from collections import Counter
def solution(strArr):
    answer = 0
    a = []
    for s in strArr:
        a.append(len(s))
        
    count = Counter(a)
    
    return max(count.values())