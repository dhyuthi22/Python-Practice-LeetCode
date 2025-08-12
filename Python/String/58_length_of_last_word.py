# 58_length_of_last_word.py
# Title: Length Of Last Word
# Difficulty: Easy
# Link: https://leetcode.com/problems/length-of-last-word
# Description: Given a string s consisting of words and spaces, return the length of the last word in the string.

# Solution:
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        i = len(s) - 1
        while i >= 0 and s[i] == ' ':
            i = i-1

        while i >= 0 and s[i] != ' ':
            length = length+1
            i = i-1