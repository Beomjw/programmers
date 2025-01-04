def solution(X, Y):
    answer = ''
    a = [0,0,0,0,0,0,0,0,0,0]
    b = [0,0,0,0,0,0,0,0,0,0]
    
    for i in X:
        value = int(i)
        a[value] += 1
    
    for j in Y:
        value = int(j)
        b[value] += 1
    
    for z in range(9, -1, -1):
        value = str(z) * min(a[z],b[z]) # 중복된 숫자 몇 번 추가할지
        answer += value
    
    if(len(answer) == 0):
        return '-1'
    
    if(answer[0] == '0'):
        return '0'
    
    return answer