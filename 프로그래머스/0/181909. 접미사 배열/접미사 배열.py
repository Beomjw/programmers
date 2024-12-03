def solution(my_string):
    answer = []
    l = len(my_string) # l = 6
    for i in range(l): # 0 1 2 3 4 5 6
        answer.append(my_string[i:])
    answer.sort()
    return answer