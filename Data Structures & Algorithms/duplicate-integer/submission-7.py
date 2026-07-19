class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       
       for i in range(len(nums) - 1):
        if nums[i] <= nums[i + 1]:
            nums[i] , nums[i + 1] = nums[i + 1] , nums[ i]
            # Now the swapping is done

            if nums[i] == nums[i + 1]:
                return True

            return False