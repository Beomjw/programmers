def solution(t, p):
    answer = 0
    number = []
    l = len(p) # "271" 3 
    for i in range(len(t)-l+1): # "3141592" 7
        number.append(t[i:l+i]) #012 #123
        
    for n in number:
        if int(n) <= int(p):
            answer += 1
            
    return answer