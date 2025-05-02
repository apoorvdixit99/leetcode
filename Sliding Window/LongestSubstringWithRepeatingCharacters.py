'''
Title - 3. Longest Substring Without Repeating Characters
Link - https://leetcode.com/problems/longest-substring-without-repeating-characters/
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        a = 0
        n = len(s)
        result = 0
        char_set = set()
        for b in range(n):
            while s[b] in char_set:
                char_set.remove(s[a])
                a += 1
            char_set.add(s[b])
            result = max(result, b - a + 1)
        return result

