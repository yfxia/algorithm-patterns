# On each day, you may decide to buy and/or sell the stock.
# You can only hold at most one share of the stock at any time.
# However, you can sell and buy the stock multiple times on the same day, ensuring you never hold more than one share of the stock.
# Find and return the maximum profit you can achieve.
# Input: prices = [7,1,5,3,6,4]
# Output: 7
# min_price doesn't hold, because we can buy/sell multiple times

def max_stock_profit(prices):
    # invariant: greedily capture each time price rises
    max_profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            max_profit += prices[i] - prices[i - 1]
    return max_profit

print(max_stock_profit([7, 1, 5, 3, 6, 4]))