# 1_two_sum.py
# Title: Two Sum
# Difficulty: Easy
# Link: https://leetcode.com/problems/two-sum
# Description: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# Solution:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = {}
        for index ,num in enumerate(nums):
            complement = target - num
            if complement in output:
                return[output[complement],index]
            output[num] = index
        