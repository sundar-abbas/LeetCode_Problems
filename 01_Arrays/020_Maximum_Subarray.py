class Solution(object):
    def Maximum_Subarray(self , nums):
        current_sum = nums[0]
        maximum_sum = nums[0]
        for i in nums[1:]:
            if current_sum < 0:
                current_sum = 0
            current_sum += i
            if current_sum > maximum_sum:
                maximum_sum = current_sum
        return maximum_sum

sol = Solution()
print(sol.Maximum_Subarray([-2,1,-3,4,-1,2,1,-5,4]))
print(sol.Maximum_Subarray([1]))
print(sol.Maximum_Subarray([5,4,-1,7,8]))