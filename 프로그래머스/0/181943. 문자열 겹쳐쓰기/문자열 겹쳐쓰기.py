def solution(my_string, overwrite_string, s):
    o = len(overwrite_string)
    m = len(my_string)
    return my_string[0:s] + overwrite_string + my_string[s+o:]