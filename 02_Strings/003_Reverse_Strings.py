class Solution(object):
    def reverse_string(self , s):
        temp_val = 0
        right = 0
        left = len(s) - 1
        while right < left:
            temp_val = s[right]
            s[right] = s[left]
            s[left] = temp_val
            right += 1
            left -= 1
        return s

sol = Solution()
print(sol.reverse_string(["A","B","B","A","S"]))
print(sol.reverse_string(["S","U","N","D","A","R"]))