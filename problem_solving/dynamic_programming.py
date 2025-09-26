"""DP examples: Fibonacci (bottom-up), Knapsack 0/1 (value only)."""

def fib_dp(n: int) -> int:
    if n <= 1: return n
    a,b = 0,1
    for _ in range(2,n+1):
        a,b = b,a+b
    return b

def knapsack_01(weights, values, capacity):
    n = len(weights)
    dp = [0]*(capacity+1)
    for i in range(n):
        w, v = weights[i], values[i]
        for c in range(capacity, w-1, -1):
            dp[c] = max(dp[c], dp[c-w]+v)
    return dp[capacity]

if __name__ == "__main__":
    print(fib_dp(20))
    print(knapsack_01([2,3,4,5], [3,4,5,8], 5))  # 8
