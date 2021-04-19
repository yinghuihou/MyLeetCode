# Definition for singly-linked list.
from typing import List


def main():
    print(maxProfit([1, 2, 1, 1]))


def maxProfit(nums: List[int]) -> int:
    n = len(nums)
    if n <= 0:
        return 0
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0], nums[1])

    # dp数组,分两列，第一列为当天偷了的最大收益，第二列为当天未偷的最大收益
    # 初始化，第一间偷了，那收益就是 （第一间的资产），如果未偷则为0

    dp = [[nums[0], 0] for i in range(n - 1)]
    mp = [[nums[1], 0] for i in range(n)]

    print(dp)
    print(mp)

    for i in range(1, n):
        # 第i间偷了的最大收益: 1、前前一间已经偷过，加上当前的收益
        # 第i间未偷最大收益：1、前一间偷过，即前一间的最大收益
        # 整体最大收益即：两者取最大

        if i < n - 1:
            dp[i][0] = dp[i - 1][1] + nums[i]
            dp[i][1] = max(dp[i - 1][0], dp[i - 1][1])
        if i > 1:
            mp[i][0] = mp[i - 1][1] + nums[i]
            mp[i][1] = max(mp[i - 1][0], mp[i - 1][1])

    result1 = max(dp[n - 2][0], dp[n - 2][1])
    result2 = max(mp[n - 1][0], mp[n - 1][1])

    return max(result1, result2)


if __name__ == '__main__':
    main()
