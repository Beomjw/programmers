def solution(a, b):
    answer = 0
    a = str(a)
    b = str(b)
    ab = int(a + b)
    eab = 2 * int(a) * int(b)
    if ab > eab:
        return ab
    else:
        return eab
