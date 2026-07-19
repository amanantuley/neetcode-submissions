class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        n = len(nums)

        for i in nums:
            if i > n/2:
                return i
                

