class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        for i in range(len(nums)):
            if nums[i] == k >= n/2 :
                return True 
        
        return False