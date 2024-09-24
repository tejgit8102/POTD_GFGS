''' 
Problem of the Day 15 - 24th Sep 2024

Smallest window in a string containing all the characters of another string

Given two strings s and p. Find the smallest window in the string s consisting of all the characters(including duplicates) of the string p.  
Return "-1" in case there is no such window present. In case there are multiple such windows of same length, return the one with the least starting index.

Note : All characters are in Lowercase alphabets. 

Example:

Input: s = "timetopractice", p = "toc"

Output: toprac

Explanation: "toprac" is the smallest substring in which "toc" can be found.

'''

#Code

class Solution:
    def smallestWindow(self, s, p):
        if len(p) > len(s):
            return "-1"

        target_freq = {}
        for char in p:
            target_freq[char] = target_freq.get(char, 0) + 1
        
        start, min_len, min_start = 0, float('inf'), 0
        matched = 0
        window_freq = {}
        
        for end in range(len(s)):
            char = s[end]
            window_freq[char] = window_freq.get(char, 0) + 1

            if char in target_freq and window_freq[char] <= target_freq[char]:
                matched += 1

            while matched == len(p):
                window_size = end - start + 1
                if window_size < min_len:
                    min_len = window_size
                    min_start = start

                start_char = s[start]
                window_freq[start_char] -= 1
                if start_char in target_freq and window_freq[start_char] < target_freq[start_char]:
                    matched -= 1
                start += 1
        
        if min_len == float('inf'):
            return "-1"
        
        return s[min_start:min_start + min_len]