''' 
Problem of the Day 18 - 27th Sep 2024

K Sized Subarray Maximum

Given an array arr[] and an integer k. Find the maximum for each and every contiguous subarray of size k.

Example:

Input: k = 3, arr[] = [1, 2, 3, 1, 4, 5, 2, 3, 6]

Output: [3, 3, 4, 5, 5, 5, 6] 

Explanation: 

1st contiguous subarray = [1 2 3] max = 3
2nd contiguous subarray = [2 3 1] max = 3
3rd contiguous subarray = [3 1 4] max = 4
4th contiguous subarray = [1 4 5] max = 5
5th contiguous subarray = [4 5 2] max = 5
6th contiguous subarray = [5 2 3] max = 5
7th contiguous subarray = [2 3 6] max = 6

'''

#Code

from collections import deque

class Solution:
    
    def max_of_subarrays(self, k, arr):
        n = len(arr)
        dq = deque()
        result = []
        
        for i in range(n):
            if dq and dq[0] < i - k + 1:
                dq.popleft()
            
            while dq and arr[dq[-1]] < arr[i]:
                dq.pop()
            
            dq.append(i)
            
            if i >= k - 1:
                result.append(arr[dq[0]])
        
        return result