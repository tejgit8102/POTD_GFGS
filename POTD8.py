''' 
Problem of the Day 8 - 17th Sep 2024

Minimize the Heights II

Given an array arr[] denoting heights of N towers and a positive integer K.

For each tower, you must perform exactly one of the following operations exactly once.

Increase the height of the tower by K
Decrease the height of the tower by K
Find out the minimum possible difference between the height of the shortest and tallest towers after you have modified each tower.

Note: It is compulsory to increase or decrease the height by K for each tower. After the operation, the resultant array should not contain any negative integers.

Example :

Input: k = 2, arr[] = {1, 5, 8, 10}

Output: 5

Explanation: The array can be modified as {1+k, 5-k, 8-k, 10-k} = {3, 3, 6, 8}.The difference between the largest and the smallest is 8-3 = 5.

'''
#Code

class Solution:
    def getMinDiff(self, arr, k):
        n = len(arr)
        arr.sort()
        ans = arr[n - 1] - arr[0]
        tempmin = arr[0]
        tempmax = arr[n - 1]

        for i in range(1, n):
            if arr[i] < k or arr[n - 1] < k:
                continue
            tempmin = min(arr[0] + k, arr[i] - k)
            tempmax = max(arr[i - 1] + k, arr[n - 1] - k)
            ans = min(ans, tempmax - tempmin)

        return ans

        
        return min(ans, largest - smallest)
