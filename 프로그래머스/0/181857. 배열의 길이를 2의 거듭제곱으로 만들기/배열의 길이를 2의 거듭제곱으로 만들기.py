def solution(arr):
    # 2의 정수 거듭제곱 
    # 2 4 8 16 32 64 128 256 512 1024
    # [1, 2, 3, 4, 5, 6] 길이 6
    
    two = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    l = len(arr) # 6
    
    for t in range(len(two)): # 0 1 2 3 4 5 6 7 8 9
        if l <= two[t]: # 6 > 2 -> 6 > 4 -> 6 < 8 
            arr.extend([0] * (two[t] - l))
            break         
            
    return arr