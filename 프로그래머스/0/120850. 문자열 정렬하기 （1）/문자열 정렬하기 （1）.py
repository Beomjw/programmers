import re

def solution(my_string):
    answer = []
    answer = re.findall(r'\d', my_string)
    return sorted(int(i) for i in answer)