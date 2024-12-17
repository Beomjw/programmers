def solution(arr):
    # [[5, 192, 33], arr[0][0] arr[0][1] arr[0][2]
    # [192, 72, 95], arr[1][0] arr[1][1] arr[1][2]
    # [33, 95, 999]] arr[2][0] arr[2][1] arr[2][2]
    # arr[2][0] == arr[0][2] == 33
    # arr[2][1] == arr[1][2] == 65
    l = len(arr) # 3
    for i in range(l): # 0 1 2 
        for j in range(l): # 0 1 2
            if arr[i][j] != arr[j][i]:
                return 0       
    return 1