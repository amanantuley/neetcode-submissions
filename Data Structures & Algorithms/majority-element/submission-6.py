class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        n = len(nums)

        for i in range(n-1):
            if i > n/2:
                return i
                

