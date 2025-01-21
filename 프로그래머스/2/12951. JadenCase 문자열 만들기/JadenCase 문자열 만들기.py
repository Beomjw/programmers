def solution(s):
    answer = ''
    is_start_of_word = True
        
    for c in s:
        if is_start_of_word:
            if c.isalpha():
                answer += c.upper()
            else:
                answer += c
            is_start_of_word = False
        else:
            answer += c.lower()
        
        if c == ' ':
            is_start_of_word = True
            
    return answer