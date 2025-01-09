def solution(new_id):
    
    new_id = new_id.lower()
    
    answer = ''
    for n in new_id:
        if n.isalnum() or n in '-_.':
            answer += n
    
    while '..' in answer:
        answer = answer.replace('..', '.')
    
    if answer and answer[0] == '.':
        answer = answer[1:]
    if answer and answer[-1] == '.':
        answer = answer[:-1]
    
    if not answer:
        answer = 'a'
    
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    
    while len(answer) < 3:
        answer += answer[-1]
            
    return answer