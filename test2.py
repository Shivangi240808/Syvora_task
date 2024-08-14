def max_average(nums, k):
    def can_find_subarray(mid):
        # Subtract mid from each element and check for a valid subarray sum
        prefix_sum = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1] - mid
            
        min_prefix_sum = 0
        for i in range(k, len(nums) + 1):
            if prefix_sum[i] - min_prefix_sum >= 0:
                return True
            min_prefix_sum = min(min_prefix_sum, prefix_sum[i - k + 1])
        
        return False

    low, high = min(nums), max(nums)
    epsilon = 1e-5
    
    while high - low > epsilon:
        mid = (low + high) / 2
        if can_find_subarray(mid):
            low = mid
        else:
            high = mid
            
    return low

nums = [1, 12, -5, -6, 50, 3]
k = 4
result = max_average(nums, k)
print(f"The maximum average value is: {result:.5f}")