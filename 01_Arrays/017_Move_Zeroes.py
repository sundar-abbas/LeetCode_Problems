class Solution(object):
    def MoveZeroes(self , nums):
        write_ptr = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[write_ptr] = nums[i]
                write_ptr +=1
        for u in range(write_ptr , len(nums)):
            nums[u] = 0
        return nums    
            
sol = Solution()
print(sol.MoveZeroes([0,0,1,1])) 