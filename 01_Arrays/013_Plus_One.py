class Solution(object):
    def plusOne(self, digits):
        for i in range(len(digits)-1,-1,-1):  # Length(n-1) , Stop(-1) , Step (-1)
            if digits[i] < 9:
                digits[i]+=1
                return digits
            digits[i] = 0
        return [1] + digits

sol = Solution()
print(sol.plusOne([1,2,3,4,5,6,7,8,8]))        
print(sol.plusOne([1,2,3,4,5,6,7,8,9]))        
print(sol.plusOne([9,9,9]))        