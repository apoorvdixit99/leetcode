'''
Title - 1. Two Sum
Link - https://leetcode.com/problems/two-sum/
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i,num in enumerate(nums):
            other_num = target - num
            if other_num in prevMap:
                return [prevMap[other_num], i]
            prevMap[num] = i
        return None
        