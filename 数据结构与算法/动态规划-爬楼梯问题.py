
# 递归暴力解法
def climb_1(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return climb_1(n - 1) + climb_1(n - 2)


print(climb_1(10))




# 记忆化搜索解法（递归+缓存）
def climb_2(n, memo=None):
    if memo is None:
        memo = {}
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n in memo:
        return memo[n]

    memo[n] = climb_2(n - 1, memo) + climb_2(n - 2, memo)
    return memo[n]

print(climb_2(20))


# 动态规划
def climb_3(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    dp = [0] * (n + 1)    # dp[i] = 到第i级的走法数
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

print(climb_3(1000000))