'''
Title - 76. Minimum Window Substring
Link - https://leetcode.com/problems/minimum-window-substring/
'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        minLength = float("inf")
        result = [-1,-1]
        n = len(s)
        l = 0
        
        count_t = {}
        for ch in t:
            count_t[ch] = count_t.get(ch, 0)+1
        have = 0
        need = len(count_t)
        
        def allCharIncluded(count_s, count_t):
            for ch, freq in count_t.items():
                if freq > count_s.get(ch, 0):
                    return False
            return True
        
        count_s = {}
        for r, ch in enumerate(s):
            count_s[ch] = count_s.get(ch, 0) + 1
            if ch in count_t and count_t[ch]==count_s[ch]:
                have += 1
            while have == need:
                length = r-l+1
                if length > 0 and length < minLength:
                    minLength = length
                    result = [l,r+1]
                count_s[s[l]] = count_s.get(s[l]) - 1
                if s[l] in count_t and count_s[s[l]]<count_t[s[l]]:
                    have -= 1
                l += 1
        
        return s[result[0]:result[1]]
        