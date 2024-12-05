def solution(arr, idx):
    answer = 0
    for a in range(len(arr)):
        if a >= idx:
            if arr[a] == 1:
                return a
    return -1