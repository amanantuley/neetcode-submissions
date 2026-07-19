class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashset = set()
        for i in range(len(nums)):
            if nums[i] == k >= 1 :
                return True 
        
        return False