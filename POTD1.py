'''
Problem of the Day 1 - 10th Sep 2024
Circle of strings:
Given an array arr of lowercase strings, determine if the strings can be chained together to form a circle.
A string X can be chained together with another string Y if the last character of X is the same as the first character of Y. 
If every string of the array can be chained with exactly two strings of the array(one with the first character and the second with the last character of the string), 
it will form a circle.
For example, for the array arr[] = {"for", "geek", "rig", "kaf"} the answer will be Yes as the given strings can be chained as "for", "rig", "geek" and "kaf" '''

#Code
from collections import defaultdict

class Solution:
    def isCircle(self, arr):
        def dfs(node, visited, graph):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, visited, graph)

        graph = defaultdict(list)
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)

        for word in arr:
            first_char = word[0]
            last_char = word[-1]
            graph[first_char].append(last_char)
            out_degree[first_char] += 1
            in_degree[last_char] += 1

        for char in set(in_degree.keys()).union(set(out_degree.keys())):
            if in_degree[char] != out_degree[char]:
                return 0

        start_char = arr[0][0]
        
        visited = set()
        dfs(start_char, visited, graph)

        for char in set(in_degree.keys()).union(set(out_degree.keys())):
            if char not in visited and (in_degree[char] > 0 or out_degree[char] > 0):
                return 0

        return 1

import sys

sys.setrecursionlimit(10**6)
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        A = input().split()

        ob = Solution()
        print(ob.isCircle(A))

