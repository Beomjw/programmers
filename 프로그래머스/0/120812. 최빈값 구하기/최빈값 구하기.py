from collections import Counter

def solution(array):
    count = Counter(array)
    
    m = max(count.values())
    
    modes = [key for key, value in count.items() if value == m]
    
    if len(modes) >= 2:
        answer = -1
    else:
        answer = modes[0]
    
    return answer

