class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        mid = (end + start) / 2

        for i in range(len(nums)):
            if target == mid:
                return mid
            elif mid > target:
                start = 0
                end = mid
            else:
                start = mid + 1
                end = len(nums) - 1

