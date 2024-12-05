def solution(my_string, indices):
    answer = ''
    indices.sort()
    # "apporoograp e m m e m p r s"
    # "0123456789101112131415161718"
    # "01 3  6   1011      1516"
    # "  p ro gra    m m e     r s"
    # "programmers"
    for s in range(len(my_string)):
        if s not in indices:
            answer += my_string[s]
        
    return answer