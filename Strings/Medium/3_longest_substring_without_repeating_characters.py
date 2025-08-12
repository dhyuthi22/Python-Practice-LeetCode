# 3_longest_substring_without_repeating_characters.py
# Title: Longest Substring Without Repeating Characters
# Difficulty: Easy
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters
# Description: Given a string s, find the length of the longest substring without duplicate characters.

# Solution:
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char = set()
        left = 0
        s_len = 0
        for right in range(len(s)):
            while s[right] in char:
                char.remove(s[left])
                left = left + 1
            
            char.add(s[right])
            s_len = max(s_len, right-left+1)
            
        return s_len