class Solution(object):
    def runningSum(self, nums):
        for i in range(1 , len(nums)):
            nums[i] += nums[i - 1]    
        return nums    

sol = Solution()        
print(sol.runningSum([1,2,3,4,5]))        
print(sol.runningSum([9,8,7,6,5,4]))        