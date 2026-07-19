class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        l = 0
        r = len(s) - 1 
        def rev(l , r):
            while l < r:
                if s[l].lower() != s[r].lower():
                    return False
                    l = l + 1
                    r = r - 1
            
        return True






    def aplhaNum(self , c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))