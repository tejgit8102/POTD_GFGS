''' 
Problem of the Day 17 - 26th Sep 2024

Roof Top

You are given the heights of consecutive buildings. You can move from the roof of a building to the roof of the next adjacent building. 
You need to find the maximum number of consecutive steps you can put forward such that you gain an increase in altitude with each step.

Example:

Input: arr[] = [1, 2, 2, 3, 2]

Output: 1

Explanation: 1, 2, or 2, 3 are the only consecutive buildings with increasing heights thus maximum number 
of consecutive steps with an increase in gain in altitude would be 1 in both cases.

'''

#Code

class Solution:
    
    def maxStep(self, arr):
        max_steps = 0
        current_steps = 0
        
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                current_steps += 1
                max_steps = max(max_steps, current_steps)
            else:
                current_steps = 0
        
        return max_steps
