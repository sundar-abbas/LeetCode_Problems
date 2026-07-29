class Solution(object):
    def removeElement(self, nums, val):
        k = 0
        for x in nums[:]:
            if x == val:
                nums.remove(x)
        k = len(nums)
        return k       
