'''
Problem of the Day 2 - 11th Sep 2024

Minimum Cost of ropes
Given an array arr containing the lengths of the different ropes, we need to connect these ropes to form one rope. The cost to connect two ropes is equal to sum of their lengths. The task is to connect the ropes with minimum cost.  

Examples:

Input: arr[] = [4, 3, 2, 6]
Output: 29
Explanation: We can connect the ropes in following ways.
1) First connect ropes of lengths 2 and 3. Which makes the array [4, 5, 6]. Cost of this operation 2 + 3 = 5. 
2) Now connect ropes of lengths 4 and 5. Which makes the array [9, 6]. Cost of this operation 4 + 5 = 9.
3) Finally connect the two ropes and all ropes have connected. Cost of this operation 9 + 6 =15
Total cost for connecting all ropes is 5 + 9 + 15 = 29. This is the optimized cost for connecting ropes. 
Other ways of connecting ropes would always have same or more cost. For example, if we connect 4 and 6 first 
(we get three rope of 3, 2 and 10), then connect 10 and 3 (we gettwo rope of 13 and 2). Finally we connect 13 and 2. 
Total cost in this way is 10 + 13 + 15 = 38.

'''

#Code

import heapq
from typing import List

class Solution:
    def minCost(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0
        
        heapq.heapify(arr)
        total_cost = 0
        
        while len(arr) > 1:
            first = heapq.heappop(arr)
            second = heapq.heappop(arr)
            cost = first + second
            total_cost += cost
            heapq.heappush(arr, cost)
        
        return total_cost
