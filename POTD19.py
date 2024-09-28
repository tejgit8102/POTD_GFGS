''' 
Problem of the Day 19 - 28th Sep 2024

Minimal Cost

There is an array arr of heights of stone and Geek is standing at the first stone and can jump to one of the following: 
Stone i+1, i+2, ... i+k stone, where k is the maximum number of steps that can be jumped and cost will be |hi-hj| is incurred, 
where j is the stone to land on. Find the minimum possible total cost incurred before the Geek reaches the last stone.

Example:

Input: k = 3, arr[]= [10, 30, 40, 50, 20]
Output: 30

Explanation: Geek will follow the path 1->2->5, the total cost would be | 10-30| + |30-20| = 30, which is minimum

'''

#Code

class Solution:
    def minimizeCost(self, k, arr):
        n = len(arr)
        dp = [float('inf')] * n
        dp[0] = 0
        
        for i in range(n):
            for j in range(1, k+1):
                if i + j < n:
                    dp[i + j] = min(dp[i + j], dp[i] + abs(arr[i] - arr[i + j]))
        
        return dp[-1]