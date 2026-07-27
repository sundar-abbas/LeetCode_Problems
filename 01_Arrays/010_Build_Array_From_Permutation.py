class Solution(object):
    def buildArray(self, nums):
        ans = []
        for num in range(0 , len(nums)):
            ans.append(nums[nums[num]])
        return ans