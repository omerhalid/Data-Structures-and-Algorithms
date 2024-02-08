def maxProfit(prices):
    if not prices:
        return 0

    first_buy, second_buy = float('-inf'), float('-inf')
    first_sell, second_sell = 0, 0

    for price in prices:
        first_buy = max(first_buy, -price)  # Maximize the negative profit after the first buy
        first_sell = max(first_sell, first_buy + price)  # Maximize the profit after the first sell
        second_buy = max(second_buy, first_sell - price)  # Maximize the profit after the second buy
        second_sell = max(second_sell, second_buy + price)  # Maximize the profit after the second sell

    return second_sell

# Example usage
print(maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))  # Output: 6
