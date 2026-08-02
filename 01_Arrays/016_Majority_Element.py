class Solution(object):
    def MajorityElement(self , nums):
        count = 0
        majority_element = None
        for num in nums:
            if count == 0:
                majority_element = num
            count += 1 if majority_element == num else -1
            
            if nums.count(majority_element) > len(nums) // 2:
                return majority_element

        return -1

sol = Solution()
print(sol.MajorityElement([1,2,3,4,5,6,7,8,9,1]))        
print(sol.MajorityElement([1,2,3,4,5,6,7,8,9,9]))        
print(sol.MajorityElement([1,2,3,4,5,1,1,1,1,1]))        
print(sol.MajorityElement([2,2,1,2]))
                
        