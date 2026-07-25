class Solution(object):
    def shuffle(self, nums, n):
        result = []
        X = nums[:n]
        Y = nums[n:]
        return [val for pair in zip(X,Y) for val in pair]

sol = Solution()
print(sol.shuffle([1,2,3,"Abbas","Ayesha","Muhammad"],3))