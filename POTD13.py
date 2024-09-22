''' 
Problem of the Day 13 - 22nd Sep 2024

Longest Prefix Suffix

Given a string of characters, find the length of the longest proper prefix which is also a proper suffix.

NOTE: Prefix and suffix can be overlapping but they should not be equal to the entire string.

Examples :

Input: str = "abab"
Output: 2
Explanation: "ab" is the longest proper prefix and suffix.

'''

#Code

class Solution:
    def lps(self, s):
        n = len(s)
        lps_arr = [0] * n
        length = 0
        i = 1
        
        while i < n:
            if s[i] == s[length]:
                length += 1
                lps_arr[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps_arr[length - 1]
                else:
                    lps_arr[i] = 0
                    i += 1
        
        return lps_arr[-1]
