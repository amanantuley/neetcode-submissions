class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + (r - 1) // 2

            if nums[mid-1] > nums[mid] and mid > 0:
                r = mid - 1
            elif nums[mid] > nums[mid + 1] and mid < len(nums) - 1:
                l = mid + 1
            else :
                return mid

