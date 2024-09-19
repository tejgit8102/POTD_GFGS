''' 
Problem of the Day 10 - 19th Sep 2024

Reverse Words

Given a String str, reverse the string without reversing its individual words. Words are separated by dots.

Note: The last character has not been '.'. 

Example :

Input: str = i.like.this.program.very.much

Output: much.very.program.this.like.i

Explanation: After reversing the whole string(not individual words), the input string becomes much.very.program.this.like.i

'''
#Code

class Solution:
    
    def reverseWords(self, str):
        words = str.split('.')
        reversed_words = words[::-1]
        return '.'.join(reversed_words)