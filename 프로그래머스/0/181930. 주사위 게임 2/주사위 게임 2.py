def solution(a, b, c):
    answer = 0
    if a != b & b != c & c != a:
        return a + b + c
    elif a != b & b == c:
        return (a + b + c) * (a*a + b*b + c*c)
    elif b != c & c == a:
        return (a + b + c) * (a*a + b*b + c*c)
    elif c != a & a == b:
        return (a + b + c) * (a*a + b*b + c*c)
    elif a == b & b == c:
        return (a + b + c) * (a*a + b*b + c*c) * (a*a*a + b*b*b + c*c*c)