class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] == s[r]:
                return True
            
        return False


    def alphaNum(self , s):
        return (ord('A') <= ord(c) <= ord('Z')or
                ord('a') <= ord(c) <= ord('z')or
                ord('0') <= ord(c) <= ord('9'))