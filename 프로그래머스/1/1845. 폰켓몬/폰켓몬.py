def solution(nums):
    m = len(nums) // 2
    nums = list(set(nums))
    
    if len(nums) > m:
        return m
    elif len(nums) == m:
        return m
    else:
        return len(nums)
