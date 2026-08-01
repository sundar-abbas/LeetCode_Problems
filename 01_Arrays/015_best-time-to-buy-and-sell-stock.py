class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        trans = 0
        buy_price = prices[0]

        for sell_price in prices:
            if sell_price < buy_price:
                buy_price = sell_price
            trans = sell_price - buy_price
            if trans > profit:
                profit = trans
        return profit       
        