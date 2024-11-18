def solution(s):
    answer = []

    for w in s.split(' '):
        word = ''
        for i, c in enumerate(w):
            if i % 2 == 0:
                word += c.upper()
            else:
                word += c.lower()

        answer.append(word)
        
    return ' '.join(answer)