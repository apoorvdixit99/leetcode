'''
Title - 424. Longest Repeating Character Replacement
Link - https://leetcode.com/problems/longest-repeating-character-replacement/
'''

from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        result = 0
        l = 0
        n = len(s)
        count = {}
        maxFreq = 0

        for r in range(n):
            ch = s[r]
            count[ch] = count.get(ch, 0) + 1
            maxFreq = max(maxFreq, count[ch])

            #maxFreq does not need to be updated
            while ((r-l+1) - maxFreq) > k:
                count[s[l]] = count.get(s[l], 0) - 1
                l += 1
            
            result = max(result, r-l+1)
        
        return result
