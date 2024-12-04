def solution(my_string, s, e):
    answer = ''
    l = len(my_string) # l = 14, s = 6, e = 12
    answer = my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]
    return answer