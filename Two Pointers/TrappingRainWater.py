'''
Title - 42. Trapping Rain Water
Link - https://leetcode.com/problems/trapping-rain-water/
'''

class Solution:

    def prefixAndSuffixArrays(self, height: List[int]) -> int:

        n = len(height)
        leftMax = [0]*n
        rightMax = [0]*n
        
        leftMax[0] = 0
        for i in range(1, n):
            leftMax[i] = max(height[i-1], leftMax[i-1])

        rightMax[n-1] = 0
        for i in range(n-2, -1, -1):
            rightMax[i] = max(height[i+1], rightMax[i+1])

        result = 0
        for i in range(n):
            result += max(0, min(leftMax[i], rightMax[i]) - height[i] )
        return result

    def trap(self, height: List[int]) -> int:
        return self.prefixAndSuffixArraysOptimization(height)