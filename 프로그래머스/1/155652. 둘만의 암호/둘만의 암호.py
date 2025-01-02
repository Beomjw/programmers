def solution(s, skip, index):
    answer = ''
    alpa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] # 0 ~ 25 
    
    for j in s:
        id = alpa.index(j) 
        count = 0
        
        while count < index: # 5
            id = (id + 1) % len(alpa) 
            if alpa[id] not in skip:
                count += 1
        
        answer += alpa[id]
            
    return answer