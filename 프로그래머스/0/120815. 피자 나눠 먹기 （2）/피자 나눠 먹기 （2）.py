import math

def lcm(a, b):
    return a * b // math.gcd(a, b)

def solution(n):
    answer = 0
    return lcm(n, 6) // 6