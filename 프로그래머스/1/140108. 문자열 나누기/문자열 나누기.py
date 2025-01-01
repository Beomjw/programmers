def solution(s):
    answer = 0
    # "banana" 첫 글자 b 
    # b a 
    # 1 1
    # n a
    # 1 1
    # n a
    # 1 1
    
    first_count = 0
    other_count = 0
    
    for i in range(len(s)): # b a n a n a
        
        if first_count == other_count: # b는 first_count a는 other_count
            answer += 1
            first = s[i] 
            # first = s[i]가 실행되는 타이밍은 
            # if first_count == other_count가 참인 순간 바로 다음 문자에서 이루어짐
            # 따라서 first = n
            first_count = 0
            other_count = 0
            
        if s[i] == first: 
            first_count += 1
        else:
            other_count += 1
   
    return answer