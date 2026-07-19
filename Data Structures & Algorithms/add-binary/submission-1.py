class Solution:
    def addBinary(self, a: str, b: str) -> str:

        for i in range(len(a)):
            if a[i] == b[i] == 1 :
                return 0
            else :
                return 1
        