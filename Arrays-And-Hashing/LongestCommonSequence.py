'''
Title - 128. Longest Common Sequence
Link - https://leetcode.com/problems/longest-consecutive-sequence
'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hash_set = set(nums)

        result = 0

        for num in hash_set:
            if (num-1) not in hash_set:
                streak = 1
                while num+streak in hash_set:
                    streak += 1
                result = max(result, streak)
        
        return result