class Solution(object):
    def length_Of_Last_Word(self , s):
        s = s.split()
        for word in range(len(s) - 1 , -1 , -1):
            return len(s[word])

sol = Solution()
print(sol.length_Of_Last_Word("Sundar Abbas"))