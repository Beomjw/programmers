def solution(s):
    answer = 0
    arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i, c in enumerate(arr):
        s = s.replace(c, str(i))
    return int(s)