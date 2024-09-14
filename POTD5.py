'''
Problem of the Day 5 - 14th Sep 2024

Alternate positive and negative numbers

Given an unsorted array arr containing both positive and negative numbers. Your task is to create an array of alternate positive and negative numbers without changing the relative order of positive and negative numbers.
Note: Array should start with a positive number and 0 (zero) should be considered a positive element.

Example:

Input: arr[] = [9, 4, -2, -1, 5, 0, -5, -3, 2]
Output: 9 -2 4 -1 5 -5 0 -3 2
Explanation: Positive elements : [9,4,5,0,2]
Negative elements : [-2,-1,-5,-3]
As we need to maintain the relative order of postive elements and negative elements we will pick each element from the positive and negative and will store them. If any of the positive and negative numbersare completed. we will continue with the remaining signed elements.
The output is 9,-2,4,-1,5,-5,0,-3,2.

'''

#Code:

class Solution:

    def rearrange(self, arr):
        pos = []
        neg = []
        n = len(arr)
        
        for i in range(n):
            if arr[i] < 0:
                neg.append(arr[i])
            else:
                pos.append(arr[i])

        i = 0
        j = 0
        k = 0

        while i < len(neg) and j < len(pos):
            arr[k] = pos[j]
            j += 1
            k += 1
            arr[k] = neg[i]
            i += 1
            k += 1

        while j < len(pos):
            arr[k] = pos[j]
            j += 1
            k += 1

        while i < len(neg):
            arr[k] = neg[i]
            i += 1
            k += 1
