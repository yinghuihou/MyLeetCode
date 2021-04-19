# Definition for singly-linked list.
from typing import List


def main():
    print(maxProfit([1, 2, 3, 4, 5]))


def maxProfit(prices: List[int]) -> int:
    n = len(prices)
    if n <= 1:
        return 0

    # dp数组,分两列，第一列为持有状态时最大收益，第二列为未持有状态时最大收益
    # 初始化，第一天持有，那收益就是 （-第一天的价格），如果未持有则为0

    dp = [[-prices[0], 0]] * n

    for i in range(1, n):
        # 第i天持有时最大收益: 1、前一天已经持有，即前一天的最大收益， 2、前一天未持有，当天买入的最大收益
        # 第i天未持有最大收益：1、前一天未持有，即前一天最大收益，2、前一天持有，当天卖出的最大收益
        # 整体最大收益即：所有天数中持有和未持有中取最大，因为最大状态一直向后转移，所以取最后一个就行

        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])
        dp[i][1] = max(dp[i - 1][0] + prices[i], dp[i - 1][1])

    return max(dp[n - 1][0], dp[n - 1][1])


if __name__ == '__main__':
    main()
