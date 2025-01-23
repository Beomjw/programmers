def solution(s):
    answer = True
    count = 0
    for i in s:
        if i == "(":
            count += 1
        elif count == 0 and i == ")":
            return False
        elif i == ")":
            count -= 1
    
    if count == 0:
        return True
    else:
        return False