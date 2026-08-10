class Solution(object):
    def sortedSquares(self, nums):
        for num in range(len(nums)):
            nums[num] = nums[num] ** 2
        nums.sort()
        return nums    
        