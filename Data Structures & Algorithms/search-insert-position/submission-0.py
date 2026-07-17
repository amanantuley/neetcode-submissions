class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        res = len(nums)
        start=0
        end = len(nums) - 1
        
        while start <= end:
            mid = (start+end) // 2

            if target == nums[mid]:
                return mid
            if nums[mid] > target:
                res = mid
                end = mid - 1
            else :
                start = mid + 1

        return res