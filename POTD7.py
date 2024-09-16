''' 
Problem of the Day 7 - 16th Sep 2024

Longest valid Parentheses

Given a string str consisting of opening and closing parenthesis '(' and ')'. Find length of the longest valid parenthesis substring.

A parenthesis string is valid if:

For every opening parenthesis, there is a closing parenthesis.
Opening parenthesis must be closed in the correct order.

Example :

Input: str = ((()

Output: 2
Explaination: The longest valid parenthesis substring is "()".

'''
#Code

class Solution:
    def maxLength(self, s: str) -> int:
        stack = [-1]
        max_length = 0
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                
                if len(stack) == 0:
                    stack.append(i)
                else:
                    max_length = max(max_length, i - stack[-1])
        
        return max_length