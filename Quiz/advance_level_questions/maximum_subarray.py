def MyFuction(nums):
    """
    This function finds the maximum subarray sum using Kadane's algorithm.
    
    :param nums: List of integers
    :return: Maximum subarray sum
    """
    if not nums:
        return 0
    
    max_current = max_global = nums[0]
    
    for i in range(1, len(nums)):
        max_current = max(nums[i], max_current + nums[i])
        if max_current > max_global:
            max_global = max_current
            
    return max_global