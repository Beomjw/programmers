# 변수 i = 0
# len(i) < len(arr)일때,
# if len(stk) == 0: arr[i]

# arr = [1, 4, 2, 5, 3]
# i = 0, arr[i] = 1, stk = [] 
# i가 len(arr) 보다 작고, stk가 빈 배열이므로 arr[i]를 stk에 추가하고 i에 1을 더함

# stk = [1], i = 1, arr[1] = 4
# i가 len(arr) 보다 작고, stk에 원소가 있고, stk의 마지막 원소가 arr[1]보다 작으므로 4를 stk 뒤에 추가하고,
# i에 1을 더함

# stk = [1, 4], i = 2, arr[1] = 2
# i가 len(arr) 보다 작고, stk에 원소가 있고, stk의 마지막 원소가 arr[1]보다 크므로 마지막 원소 제거

# stk = [1], i = 2, arr[1] = 2
# i가 len(arr) 보다 작고, stk에 원소가 있고, stk의 마지막 원소가 arr[1]보다 작으므로 4를 stk 뒤에 추가하고,
# i에 1을 더함

# stk = [1, 2], i = 3, arr[3] = 5
# i가 len(arr) 보다 작고, stk에 원소가 있고, stk의 마지막 원소가 arr[1]보다 작으므로 4를 stk 뒤에 추가하고,
# i에 1을 더함

# stk = [1, 2, 5], i = 4, arr[4] = 3
# i가 len(arr) 보다 작고, stk에 원소가 있고, stk의 마지막 원소가 arr[1]보다 크므로 마지막 원소 제거

# stk = [1, 2], i = 4, arr[4] = 3
# i가 len(arr) 보다 작고, stk에 원소가 있고, stk의 마지막 원소가 arr[1]보다 작으므로 4를 stk 뒤에 추가하고,
# i에 1을 더함

# stk = [1, 2, 3], i = 5
# i가 len(arr)와 같으므로 작업 종료

def solution(arr):
    stk = []
    i = 0
    while i < len(arr):
        if len(stk) == 0:
            stk.append(arr[i])
            i += 1
        else:
            if stk[-1] < arr[i]:
                stk.append(arr[i])
                i += 1
            else:
                stk.pop()
    return stk