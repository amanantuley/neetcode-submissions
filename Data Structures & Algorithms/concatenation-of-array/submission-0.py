class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        ans = []

        for i in nums:
            ans.add(i)
        for j in nums:
            ans.add(j)

        return ans