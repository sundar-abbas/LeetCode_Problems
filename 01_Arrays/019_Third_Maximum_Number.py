class Solution(object):
    def third_maximum_number(self , nums):
        unique_list = sorted(list(set(nums)))
        if len(unique_list) < 3:
            return unique_list[-1] 
        return unique_list[-3]

sol = Solution()
print(sol.third_maximum_number([2,2,3,4,5,10,1])) 
print(sol.third_maximum_number([10,11])) 