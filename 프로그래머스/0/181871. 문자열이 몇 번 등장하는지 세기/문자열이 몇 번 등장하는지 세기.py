def solution(myString, pat):
    count = 0
    # "banana"
    # "ana"
    start = 0
    while True:
        index = myString.find(pat, start)
        if index == -1:
            break
        else:
            count += 1
            start = index + 1
            
    return count