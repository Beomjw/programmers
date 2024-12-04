def solution(my_string, is_prefix):
    answer = 0
    string = []
    for i in range(len(my_string)):
        string.append(my_string[:i])

    for s in string:
        if s == is_prefix:
            return 1
    return 0