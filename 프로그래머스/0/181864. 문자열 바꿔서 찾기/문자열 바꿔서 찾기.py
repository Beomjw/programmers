def solution(myString, pat):
    answer = 0
    result = myString.replace('A', 'X').replace('B', 'A').replace('X', 'B')
    # "ABBAA"
    # "XBBXX"
    # "XAAXX"
    # "BAABB"
    if pat in result:
        return 1
    else:
        return 0