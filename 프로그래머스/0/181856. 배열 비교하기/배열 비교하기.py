def solution(arr1, arr2):
    # arr1이 크면 1
    # arr2가 크면 -1
    # 같으면 0
    a1 = len(arr1)
    a2 = len(arr2)
    sum1 = sum(arr1)
    sum2 = sum(arr2)
    if a1 > a2:
        return 1
    elif a1 < a2:
        return -1
    elif a1 == a2:
        if sum1 > sum2:
            return 1
        elif sum1 < sum2:
            return -1
        elif sum1 == sum2:
            return 0