def solution(dartResult):
    answer = 0
    # 점수 Single 점수 Double 점수 Triple
    # 점수 점수제곱 점수세제곱
    # 스타상* 해당 점수와 바로 전에 얻은 점수를 2배로 만듬
    # 아차상# 해당 점수가 마이너스 됨
    
    # 1S2D*3T = 37	
    # (1 * 2) + ((2*2) * 2)  + (3*3*3)
    
    n = ''
    score = []
    for i in dartResult: # 1S2D*3T
        if i.isnumeric(): # 1 # 2 # 3
            n += i
        
        elif i == 'S':
            n = int(n)**1
            score.append(n) # [1]
            n = ''
    
        elif i == 'D':
            n = int(n)**2
            score.append(n) # [1, 4]
            n = ''
    
        elif i == 'T':
            n = int(n)**3
            score.append(n) # [27]
            n = ''
    
        elif i == '*':
            if len(score) > 1: # [2, 8]
                score[-2] = score[-2] * 2
                score[-1] = score[-1] * 2
            else:
                score[-1] = score[-1] * 2
    
        elif i == '#':
            score[-1] = score[-1] * -1
        
    return sum(score) # [2, 8, 27]