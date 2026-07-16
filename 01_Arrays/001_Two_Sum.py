from typing import List
class Solution(object):
    def twoSum(self, nums : List[int], target:int) -> List[int]:
        for x in range(len(nums)):
            for y in range(x + 1 ,len(nums)):
                if nums[x] + nums[y] == target:
                    return [x,y]
                
if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2,7,11,15],9))                 
    print(sol.twoSum([3,2,4],6))                 
    print(sol.twoSum([3,3],6))                 