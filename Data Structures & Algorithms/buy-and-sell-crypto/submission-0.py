class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price: int = prices[0]
        max_profit: int = 0
        ## Skip first element
        for day, price in enumerate(prices):
            min_price = min(price, min_price)

            max_profit = max(max_profit, price-min_price)
            print(day, price, min_price, max_profit)
        return max_profit