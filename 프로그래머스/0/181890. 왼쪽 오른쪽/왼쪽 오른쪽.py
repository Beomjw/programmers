def solution(str_list):
    first = False
    for i in range(len(str_list)):
        if str_list[i] == 'l' and not first:
            first = True
            return str_list[:i]
        elif str_list[i]  == 'r' and not first:
            first = True
            return str_list[i+1:]
    return []