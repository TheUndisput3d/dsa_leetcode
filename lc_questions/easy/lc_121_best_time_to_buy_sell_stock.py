from typing import List

## Brute Force Approach
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Time Complexity: O(n^2), where n is the number of days (length of the prices list).
                         Each day is paired with every future day, leading to a nested loop.

        Space Complexity: O(1), constant space is used — only one variable for max profit.
        """

        n = len(prices)
        max_profit = 0

        # Try every possible pair of days (i < j)
        for i in range(n):
            for j in range(i + 1, n):
                # Calculate profit for buying on day i and selling on day j
                curr_profit = prices[j] - prices[i]

                # Update max profit if the current profit is higher
                max_profit = max(curr_profit, max_profit)

        # Return the highest profit found
        return max_profit


## Optimal Approach- I
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Time Complexity: O(n), where n is the number of days (length of the prices list).
                         The algorithm makes a single pass through the list.
        
        Space Complexity: O(1), only two variables are used regardless of input size.
        """

        # Initialize maximum profit to 0
        profit = 0

        # Initialize minimum buying price to infinity
        buy_price = float('inf')

        # Loop through each price in the list
        for price in prices:
            # Update the buy_price if we find a lower price
            if price < buy_price:
                buy_price = price
            else:
                # Calculate current profit and update the max profit if it's greater
                profit = max(profit, price - buy_price)

        # Return the highest profit found
        return profit


## Optimal Approach-II
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Time Complexity: O(n), where n is the number of days (length of the prices list).
                         We make only one pass through the list using two pointers.

        Space Complexity: O(1), constant space is used — only pointers and a few variables.
        """

        n = len(prices)

        # Initialize two pointers:
        # i - potential buying day, j - potential selling day
        i, j = 0, 1

        # Initialize the maximum profit
        max_profit = 0

        # Loop until the selling pointer reaches the end of the list
        while j < n:
            # Calculate the current profit if we buy at day i and sell at day j
            curr_profit = prices[j] - prices[i]

            if curr_profit < 0:
                # If current profit is negative, it means price[j] < price[i],
                # so update buying day to j (buy at a cheaper price)
                i = j
            else:
                # Update max profit if the current profit is greater
                max_profit = max(max_profit, curr_profit)

            # Move the selling pointer forward
            j += 1

        # Return the highest profit found
        return max_profit


