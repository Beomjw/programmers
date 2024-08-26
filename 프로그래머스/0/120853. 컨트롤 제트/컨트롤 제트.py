def solution(s):
    answer = []
    a = s.split()
    
    for i in a: 
        if i == "Z":
            answer.pop()
        else:
            answer.append(int(i))
        
    return sum(answer)
