def solution(my_string):
    a = 'aeiouAEIOU'
    answer = ''.join(c for c in my_string if c not in a)
    return answer