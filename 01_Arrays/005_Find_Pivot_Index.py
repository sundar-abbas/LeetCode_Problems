class Solution(object):
    def pivotIndex(self, nums):
        left_sum = 0
        total_sum = sum(nums)

        for i , num in enumerate(nums):
            right_sum = total_sum - left_sum - num

            if left_sum == right_sum :
                return i

            left_sum += num
        return -1        

sol = Solution()
print(sol.pivotIndex([1,3,6]))
print(sol.pivotIndex([1,3,2,5,6]))