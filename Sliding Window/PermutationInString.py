'''
Title - 567. Permutation in String
Link - https://leetcode.com/problems/permutation-in-string/
'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # if len(s1)>len(s2):
        #     return False
        
        # dict_s1 = {}
        # dict_s2 = {}
        # for ch in s1:
        #     dict_s1[ch] = dict_s1.get(ch, 0) + 1
        
        # for ch in s2[0:len(s1)]:
        #     dict_s2[ch] = dict_s2.get(ch, 0) + 1
        
        # if dict_s1 == dict_s2:
        #     return True
        
        # for i,ch in enumerate(s2[len(s1):]):
        #     s1_index = i
        #     s2_index = i+len(s1)
            
        #     # Remove
        #     dict_s2[s2[i]] = dict_s2[s2[i]] - 1
        #     if dict_s2[s2[i]] == 0:
        #         del dict_s2[s2[i]]

        #     # Add
        #     dict_s2[ch] = dict_s2.get(ch, 0) + 1

        #     if dict_s1 == dict_s2:
        #         return True
        
        # return False

        if len(s1)>len(s2):
            return False

        freq1 = [0]*26
        freq2 = [0]*26

        for i in range(len(s1)):
            ch1, ch2 = s1[i], s2[i]
            i1, i2 = ord(ch1)-ord('a'), ord(ch2)-ord('a')
            freq1[i1] += 1
            freq2[i2] += 1
        
        matches = 0
        for i in range(26):
            if freq1[i]==freq2[i]:
                matches+=1
            
        if matches == 26:
            return True
        
        for i, ch in enumerate(s2[len(s1):]):

            # ch starts from index len(s1)
            # i starts from 0

            # Remove ith character
            i2 = ord(s2[i])-ord('a')
            if freq2[i2] == freq1[i2]:
                matches-=1
            freq2[i2] -= 1
            if freq2[i2] == freq1[i2]:
                matches+=1
            
            # Add i+len(s1)th character
            i2 = ord(ch)-ord('a')
            if freq2[i2] == freq1[i2]:
                matches-=1
            freq2[i2] += 1
            if freq2[i2] == freq1[i2]:
                matches+=1
            
            if matches == 26:
                return True
        
        return False



