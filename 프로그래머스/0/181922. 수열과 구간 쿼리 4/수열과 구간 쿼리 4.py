# arr [0, 1, 2, 4, 3]
# [s, e, k]

# [0, 4, 1]
# 모든 i가 1의 배수
# [1, 2, 3, 5, 4]

# [0, 3, 2]
# i가 2의 배수인 index 0, 2 
# [2, 2, 4, 5, 4]

# [0, 3, 3]
# i가 3의 배수인 index 0, 3
# [3, 2, 4, 6, 4]

def solution(arr, queries):
    for s, e, k in queries:
        for a in range(s, e+1): # 0 1 2 3 4
            if a % k == 0: 
                arr[a] += 1
    return arr