from datetime import datetime

def solution(data, ext, val_ext, sort_by):
    answer = []
    sort_b = {
        "code": 0, "date": 1, "maximum": 2, "remain": 3
    }

    for d in data:
        if d[sort_b[ext]] < val_ext:
            answer.append(d)
            
    sort_key = lambda x : x[sort_b[sort_by]]
    
    answer.sort(key = sort_key)
    
    return answer