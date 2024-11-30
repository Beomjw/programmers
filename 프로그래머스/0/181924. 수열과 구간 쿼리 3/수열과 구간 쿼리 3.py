# arr [0, 1, 2, 3, 4]
# queries[[0, 3], [1, 2], [1, 4]]

# [0, 3]
# [3, 1, 2, 0, 4]

# [1, 2]
# [3, 2, 1, 0, 4]

# [1, 4]
# [3, 4, 1, 0, 2]
def solution(arr, queries):
    answer = []
    for i, j in queries:
        b = arr[i]
        arr[i] = arr[j]
        arr[j] = b
    return arr