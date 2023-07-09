class Solution:
    def maxProfit(self, prices) -> int:

        #2 ptr solution
        # Time: O(n)
        # Space: O(1)
        
        l, r = 0, 1
        max_profit = 0
        
        while r < len(prices):
            if prices[l] < prices[r]:
                current_profit = prices[r] - prices[l]
                max_profit = max(max_profit, current_profit)
            else:
                l = r
            r += 1
        return max_profit
    
sol = Solution()
result = sol.maxProfit([7,1,5,3,6,4])
print(result)
                 