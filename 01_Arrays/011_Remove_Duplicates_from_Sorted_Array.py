class Solution(object):
    def removeDuplicates(self, nums):
        unique_list = sorted(list(set(nums)))
        k = len(unique_list)
        nums[:k] = unique_list
        return k        