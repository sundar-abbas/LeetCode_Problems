class Solution(object):
    def getConcatenation(self, nums):
        ans = list(nums)
        for num in nums:
            ans.append(num)
        return ans