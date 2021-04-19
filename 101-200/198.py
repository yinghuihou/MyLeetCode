# Definition for singly-linked list.
from typing import List


def main():
    print(maxProfit([2, 7, 9, 3, 1]))


def maxProfit(prices: List[int]) -> int:
    n = len(prices)
    if n <= 0:
        return 0

    # dp数组,分两列，第一列为当天偷了的最大收益，第二列为当天未偷的最大收益
    # 初始化，第一间偷了，那收益就是 （第一间的资产），如果未偷则为0

    dp = [[prices[0], 0] for i in range(n)]
    for i in range(1, n):
        # 第i间偷了的最大收益: 1、前前一间已经偷过，加上当前的收益
        # 第i间未偷最大收益：1、前一间偷过，即前一间的最大收益
        # 整体最大收益即：两者取最大

        dp[i][0] = dp[i - 1][1] + prices[i]
        dp[i][1] = max(dp[i - 1][0], dp[i - 1][1])
       
    return max(dp[n - 1][0], dp[n - 1][1])


if __name__ == '__main__':
    main()
