def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1
coins_input = input("Enter the denominations of coins separated by space: ")
coins = list(map(int, coins_input.split()))
amount = int(input("Enter the amount: "))
print(coin_change(coins, amount))
