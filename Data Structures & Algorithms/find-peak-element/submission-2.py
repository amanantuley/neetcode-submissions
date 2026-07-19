class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        max = 0
        for i in range(len(nums)):
            for j in range(i+1 , len(nums)):
                if nums[i] == nums[j]:
                    max = nums[i]
                    return max
                elif nums[i] > nums[j]:
                    max = nums[i]
                    return max
                else:
                    max = nums[j]
                    return max
           
        return -1