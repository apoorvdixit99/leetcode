'''
Title - 49. Group Anagrams
Link - https://leetcode.com/problems/group-anagrams
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for word in strs:
            freq = [0]*26
            for ch in word:
                freq[ord(ch)-ord('a')] += 1
            group[str(freq)] = group.get(str(freq), [])
            group[str(freq)].append(word)
        return list(group.values())