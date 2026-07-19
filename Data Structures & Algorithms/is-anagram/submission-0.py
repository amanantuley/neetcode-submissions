class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Counter(s) == Counter(t)