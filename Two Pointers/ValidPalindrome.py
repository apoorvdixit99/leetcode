'''
Tile - 125. Valid Palindrome
Link - https://leetcode.com/problems/valid-palindrome/
'''

class Solution:

    def __init__(self):
        self.orda = ord('a')
        self.ordA = ord('A')
        self.ordz = ord('z')
        self.ordZ = ord('Z')
        self.ord0 = ord('0')
        self.ord9 = ord('9')

    def isAlphanumeric(self, ch):
        ordch = ord(ch)
        return ( self.orda <= ordch and ordch <= self.ordz ) or ( self.ordA <= ordch and ordch <= self.ordZ ) or ( self.ord0 <= ordch and ordch <= self.ord9 )

    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        n = len(s)
        i,j = 0,n-1
        
        while i<=j:

            # Skip non-alphanumeric characters
            while i<=j and not self.isAlphanumeric(s[i]):
                i+=1
            while j>=i and not self.isAlphanumeric(s[j]):
                j-=1
            if i>j:
                break
            elif s[i]!=s[j]:
                return False
            else:
                i+=1
                j-=1
        
        return True