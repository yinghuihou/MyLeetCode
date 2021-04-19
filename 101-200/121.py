# Definition for singly-linked list.
from typing import List


def main():
    print(maxProfit([7, 1, 5, 3, 6, 4]))


def maxProfit(prices: List[int]) -> int:
    n = len(prices)
    if n <= 1:
        return 0

    #dp数组

    dp = [0] * n

    #前i天最小的买入价格
    min = prices[0]

    for i in range(1, n):
        if min > prices[i]:
            min = prices[i]

        # 第i天的最大收益，要么当天不买卖，就是用前一天的最大收益
        # 要么就是当天卖出，然后收获一笔收益，当天卖出的话就是在之前最低点买入，卖出时收益最大，因为只能买卖一次
        dp[i] = max(dp[i - 1], prices[i] - min)
    return dp[-1]


if __name__ == '__main__':
    main()
