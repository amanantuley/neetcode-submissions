class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        n = len(nums)

        for i in range(n):
            if i > n/2:
                return nums[i]

