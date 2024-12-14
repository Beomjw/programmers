def solution(arr, n):
    l = len(arr)
    if l % 2 == 0:
        for i in range(l):
            if i % 2 != 0:
                arr[i] += n
    else:
        for i in range(l):
            if i % 2 == 0:
                arr[i] += n      
    return arr