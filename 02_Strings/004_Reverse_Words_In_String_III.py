class Solution(object):
    def reverse_words(self , s) ->str:
        return " ".join(word[::-1] for word in s.split())

sol = Solution()
print(sol.reverse_words("Sundar Abbas"))