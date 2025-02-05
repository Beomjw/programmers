def solution(s):
    zero = 0
    b = 0
    while s != '1':
        zero += s.count("0")
        s = bin(s.count("1"))[2:]
        b += 1
    
    return [b, zero]