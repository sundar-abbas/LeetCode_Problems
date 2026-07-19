class Solution(object):
    def maximumWealth(self, accounts):
        max = 0
        for x in range(0 , len(accounts)):
            current = 0
            for y in range(0 , len(accounts[x])):
                current += accounts[x][y]
                if max < current:
                    max = current
        return max    

sol = Solution()
print(sol.maximumWealth([[1,2,3,4],[9,8,2],[20,30]]))        