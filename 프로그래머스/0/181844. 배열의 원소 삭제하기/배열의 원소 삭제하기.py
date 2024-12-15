def solution(arr, delete_list):
    for a in delete_list:
        if a in arr:
            arr.remove(a)
            
    return arr