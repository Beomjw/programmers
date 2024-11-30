# [s, e, k]
# s <= i <= e
# arr[i]

# [0, 4, 2]
# [0, 1, 2, 4, 3] 중에서 2보다 크면서 가장 작은 숫자 3

# [0, 3, 2]
# [0, 1, 2, 4] 중에서 2보다 크면서 가장 작은 숫자 4

# [0, 2, 2]
# [0, 1, 2] 중에서 2보다 크면서 가장 작은 숫자 없음 -1 출력

def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        m = []
        for x in arr[s:e+1]:
            if x > k:
                m.append(x)
    
        if m:
            answer.append(min(m))
        else:
            answer.append(-1)        
    return answer