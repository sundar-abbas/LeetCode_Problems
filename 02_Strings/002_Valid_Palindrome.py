class Solution(object):
    def validPalindrome(self , s):
        cleaned = "".join(char.lower() for char in s if char.isalnum())
        return cleaned == cleaned[::-1]

sol = Solution()
print(sol.validPalindrome("A man, a plan, a canal: Panama"))
print(sol.validPalindrome("race a car"))
print(sol.validPalindrome(""))