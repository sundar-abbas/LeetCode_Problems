class Solution(object):
    def containsDuplicate(self, nums):
        seen = set() 
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

sol = Solution()
print(sol.containsDuplicate([1,1,2,4,5,7,7]))
print(sol.containsDuplicate([1,2,3,4,5]))