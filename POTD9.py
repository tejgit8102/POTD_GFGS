''' 
Problem of the Day 9 - 18th Sep 2024

Parenthesis Checker

Given an expression string x. Examine whether the pairs and the orders of {,},(,),[,] are correct in exp.
For example, the function should return 'true' for exp = [()]{}{[()()]()} and 'false' for exp = [(]).

Note: The driver code prints "balanced" if function return true, otherwise it prints "not balanced".

Example :

Input: {([])}
Output: true

Explanation: { ( [ ] ) }. Same colored brackets can form balanced pairs, with 0 number of unbalanced bracket.

'''
#Code

class Solution:
    def ispar(self, x):
        stack = []
        bracket_map = {')': '(', ']': '[', '}': '{'}
        
        for char in x:
            if char in bracket_map:
                top_element = stack.pop() if stack else '#'
                if bracket_map[char] != top_element:
                    return False
            else:
                stack.append(char)
        
        return not stack