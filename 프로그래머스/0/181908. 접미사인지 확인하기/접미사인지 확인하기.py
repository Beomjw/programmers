def solution(my_string, is_suffix):
    answer = 0
    result = []
    l = len(my_string)
    for i in range(l):
        result.append(my_string[i:])
    
    for r in result:
        if r == is_suffix:
            return 1
    return 0