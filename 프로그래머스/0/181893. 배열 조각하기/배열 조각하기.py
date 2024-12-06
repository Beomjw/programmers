def solution(arr, query):
    # [0, 1, 2, 3, 4, 5]
    # [4, 1, 2]
    # 4 짝수 이므로 뒷부분 자름 [0, 1, 2, 3, 4]
    # 1 홀수 이므로 앞부분 자름 [1, 2, 3, 4]
    # 2 짝수 이므로 뒷부분 자름 [1, 2, 3]
    
    for q in range(len(query)):
        if q % 2 == 0:
            arr = arr[:query[q]+1]
        else:
            arr = arr[query[q]:]
    return arr