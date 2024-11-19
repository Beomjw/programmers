def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        combined = bin(arr1[i] | arr2[i])[2:]
        
        combined = combined.zfill(n)

        result = combined.replace('1', '#').replace('0', ' ')
        
        answer.append(result)
    
    return answer