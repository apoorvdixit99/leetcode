'''
Title - Encode and Decode Strings
Link - https://leetcode.com/problems/encode-and-decode-strings
'''

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        result = ""
        for word in strs:
            result = str(len(word))+"#"+word
        return result

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, strr):
        # write your code here
        result = []
        index = 0
        n = len(str)
        
        while index<n:
            word_len_start = index
            while strr[index]!="#":
                index+=1
            word_len = int(str[word_len_start: index])

            result.append(
                str[index+1:index+1+word_len]
            )

            index = index+word_len+1