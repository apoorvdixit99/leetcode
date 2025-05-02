'''
Title - 239. Sliding Window Maximum
Link - https://leetcode.com/problems/sliding-window-maximum/
'''

from collections import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        max_heap = []
        result = []
        MAX, VAL, IDX = 0, 0, 1

        for index, num in enumerate(nums[0:k-1]):
            heapq.heappush(max_heap, (-num, index))
        
        for index in range(k-1,len(nums)):
            heapq.heappush(max_heap, (-nums[index], index))
            while max_heap[MAX][IDX] <= index-k:
                heapq.heappop(max_heap)
            result.append(
                -max_heap[MAX][VAL]
            )

        return result

    
