def maxCoins(nums):
    # Step 1: Pad the nums array with 1's at the beginning and end.
    nums = [1] + nums + [1]
    n = len(nums)
    
    # Step 2: Initialize a DP table where dp[i][j] is the max score we can get by bursting all balloons between i and j.
    dp = [[0] * n for _ in range(n)]
    
    # Step 3: Fill the DP table by increasing subproblem size.
    for length in range(2, n):  # length of the subarray we are considering
        for i in range(n - length):  # left boundary of the subarray
            j = i + length  # right boundary of the subarray
            for k in range(i + 1, j):  # k is the position of the last balloon to burst
                dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j])
    
    # Step 4: The final result will be in dp[0][n-1]
    return dp[0][n-1]
