def solution(a, b):
    a = str(a)
    b = str(b)
    ab = a + b
    ba = b + a
    if int(ab) > int(ba):
        return int(ab)
    else:
        return int(ba)