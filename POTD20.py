''' 
Problem of the Day 20 - 29th Sep 2024

Total count

You are given an array arr[] of positive integers and a threshold value k. 
For each element in the array, divide it into the minimum number of small integers such that each divided integer is less 
than or equal to k. Compute the total number of these integer across all elements of the array.

Example:

Input: k = 3, arr[] = [5, 8, 10, 13]

Output: 14

Explanation: Each number can be expressed as sum of different numbers less than or equal to k as 5 (3 + 2),
8 (3 + 3 + 2), 10 (3 + 3 + 3 + 1), 13 (3 + 3 + 3 + 3 + 1). So, the sum of count of each element is (2+3+4+5)=14.

'''

#Code

class Solution:
    def totalCount(self, k, arr):
        total_parts = 0
        
        for num in arr:
            # Calculate how many parts are needed for the current number
            # Equivalent to math.ceil(num / k)
            parts = (num + k - 1) // k
            total_parts += parts
        
        return total_parts