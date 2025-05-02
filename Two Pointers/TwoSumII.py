'''
Title - 167. Two Sum II - Input Array Is Sorted
Link - https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
'''

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i,j = 0,n-1
        while (i<j):
            score = numbers[i] + numbers[j]
            if score < target:
                i+=1
            elif score > target:
                j-=1
            else:
                return [i+1,j+1]
        return [None,None]