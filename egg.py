def superEggDrop(k, n):
    # Initialize dp array, where dp[i][j] is the minimum number of moves with i eggs and j floors.
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    
    # Base cases:
    # dp[0][j] = 0 for all j (0 eggs -> 0 moves)
    # dp[i][0] = 0 for all i (0 floors -> 0 moves)
    
    for i in range(1, k + 1):  # Loop for each egg
        dp[i][0] = 0  # No floors to test, so no moves
        dp[i][1] = 1  # One floor, so one move
    
    for j in range(1, n + 1):  # Loop for each floor
        dp[1][j] = j  # With 1 egg, we need to test all floors one by one
    
    # Fill the dp table
    for i in range(2, k + 1):  # Loop for each egg
        for j in range(2, n + 1):  # Loop for each floor
            low, high = 1, j
            while low + 1 < high:  # Binary search for the optimal floor to drop the egg from
                mid = (low + high) // 2
                if dp[i - 1][mid - 1] < dp[i][j - mid]:
                    low = mid
                else:
                    high = mid
            dp[i][j] = 1 + min(max(dp[i - 1][low - 1], dp[i][j - low]),
                               max(dp[i - 1][high - 1], dp[i][j - high]))
    
    return dp[k][n]
