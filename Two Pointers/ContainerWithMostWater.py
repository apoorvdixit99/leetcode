'''
Title - 11. Container With Most Water
Link - https://leetcode.com/problems/container-with-most-water/
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n,l,r = len(height), 0, len(height)-1
        result = 0
        while l<r:
            area = (r-l)*min(height[l], height[r])
            result = max(result, area)
            if height[l] <= height[r]:
                l+=1
            else:
                r-=1
        return result