class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        nums.sort()

        k = set()

        for i in nums:
            if nums[i] != val:
                k.append(nums[i])
            

        return len(k)