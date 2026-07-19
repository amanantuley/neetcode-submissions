class Solution:
    def isPalindrome(self, s: str) -> bool:
        

        def rev(l , r):
            if l < r:
                if s[l] == s[r]:
                    return True
                rev(l+1 , r -1)
            
        rev(0 , len(s) -1)