def solution(arr):
    # i = 0
    # len(arr) = 5
    # [0, 1, 1, 1, 0]
    # [0] i = 1
    # 0 != 1 
    # [0, 1] i = 2
    # 1 != 1
    # [0] i = 3
    
    i = 0
    l = len(arr)
    stk = []
    while i < l:
        if stk and stk[-1] == arr[i]:
            stk.pop()
        else:
            stk.append(arr[i])
        i += 1
    
    if stk:  
        return stk
    else:
        return [-1]