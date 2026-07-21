class Solution(object):
    def largestAltitude(self, gain):
        n = len(gain)
        mx = 0
        for i in range(n + 1):
            alt = 0
            for j in range(i):
                alt += gain[j]
            mx = max(mx, alt)
        return mx    

sol = Solution()
print(sol.largestAltitude([12,45,21,8,-1]))