class Solution(object):
    def valid_anagram(self , s , t):
        return sorted(s) == sorted(t)

sol = Solution()
print(sol.valid_anagram("anagram","gramana"))
print(sol.valid_anagram("anagram","graman"))