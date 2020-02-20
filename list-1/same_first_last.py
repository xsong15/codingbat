def same_first_last(nums):
    """
    Given an array of ints, return True if the array is 
    length 1 or more, and the first element and the last 
    element are equal.
    """
    return len(nums) >= 1 and nums[-1] == nums[0]

print(same_first_last([1, 2, 3])) #False
print(same_first_last([1, 2, 3, 1])) #True
print(same_first_last([1, 2, 1])) #True