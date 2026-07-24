class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        result = []
        mx = max(candies) 
        for x in candies:
            result.append(x + extraCandies >= mx)
        return result            
    