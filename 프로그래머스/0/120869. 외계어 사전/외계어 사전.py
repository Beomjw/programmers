def solution(spell, dic):
    answer = 0
    s = ''.join(sorted(spell))
    
    for d in dic:
        if s == ''.join(sorted(d)):
            return 1
    
    return 2