class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        #prices : list


        left = 0
        right = 1
        profit = 0

        while right < len(prices):

            if prices[left] > prices[right]:
                left = right
                right += 1

            else:
                if prices[right] - prices[left] > profit:
                    profit = prices[right] - prices[left]

            right += 1
            
        return profit