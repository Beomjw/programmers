from collections import Counter
def solution(participant, completion):
    answer = ''
    count = Counter(participant) - Counter(completion)
    
    return list(count.keys())[0]