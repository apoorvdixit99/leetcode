'''
Title - 238. Product of Array Except Self
Link - https://leetcode.com/problems/product-of-array-except-self/
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        # result = [1]*n
        result = []
        prefix = 1
        postfix = 1

        for i in range(0, n):
            # result[i] = prefix
            result.append(prefix)
            prefix = prefix * nums[i]
        
        for i in range(n-1,-1,-1):
            result[i] *= postfix
            postfix = postfix*nums[i]

        return result

        