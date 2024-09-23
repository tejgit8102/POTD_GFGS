''' 
Problem of the Day 14 - 23rd Sep 2024

Missing And Repeating

Given an unsorted array arr of of positive integers. One number 'A' from set {1, 2,....,n} is missing and one number 'B' occurs twice in array. Find numbers A and B.

Example:

Input: arr[] = [2, 2]

Output: 2 1

Explanation: Repeating number is 2 and smallest positive missing number is 1.

'''

#Code

class Solution:
    def findTwoElement(self, arr):
        n = len(arr)
        
        expected_sum = n * (n + 1) // 2
        expected_square_sum = n * (n + 1) * (2 * n + 1) // 6
        
        actual_sum = 0
        actual_square_sum = 0
        for num in arr:
            actual_sum += num
            actual_square_sum += num * num
        
        diff_sum = actual_sum - expected_sum
        diff_square_sum = actual_square_sum - expected_square_sum
        
        sum_plus = diff_square_sum // diff_sum
        
        B = (diff_sum + sum_plus) // 2
        A = B - diff_sum
        
        return [B, A]