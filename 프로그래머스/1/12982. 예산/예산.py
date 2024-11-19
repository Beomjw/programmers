def solution(d, budget):

    d.sort()
    count = 0
    total = 0
    
    for cost in d:
        if total + cost > budget:
            break
        total += cost
        count += 1
    
    return count