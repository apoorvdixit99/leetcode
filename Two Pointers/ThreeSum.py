'''
Title - Three Sum
Link - https://leetcode.com/problems/3sum/
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)

        target = 0
        n = len(nums)
        result = []

        for i in range(n-2):

            # Skip if repeated
            if i>0 and nums[i]==nums[i-1]:
                continue

            # Two sum for sorted array
            else:
                a = nums[i]
                j,k = i+1,n-1
                while j<k:
                    b,c = nums[j], nums[k]
                    score = a+b+c
                    if score<target:
                        j+=1
                    elif score>target:
                        k-=1
                    else:
                        result.append(
                            [a,b,c]
                        )
                        j+=1
                        while j<k and nums[j]==nums[j-1]:
                            j+=1
                        k-=1
                        while k>j and nums[k]==nums[k+1]:
                            k-=1

        return result
                    