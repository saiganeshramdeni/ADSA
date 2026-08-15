'''# 209. Minimum Size Subarray Sum
def minSubArrayLen( target: int, nums: list[int]) -> int:
    left = 0
    current_sum = 0
    min_length = float('inf')
        
    for right in range(len(nums)):
        current_sum += nums[right]
            
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1
                
    return min_length if min_length != float('inf') else 0
target = 4
nums = [1,4,4]
print(minSubArrayLen(target, nums))'''

'''# 713. Subarray Product Less Than K
def numSubarrayProductLessThanK( nums: List[int], k: int) -> int:
        if  k<=1:
            return 0 
        left=0
        count=0
        p=1
        for right in range(len(nums)):
            p*=nums[right]
            while p>=k:
                p//=nums[left]
                left+=1
            count+=(right -left+1)
        return count 
nums = [10,5,2,6]
k = 100
print(numSubarrayProductLessThanK(nums, k))'''