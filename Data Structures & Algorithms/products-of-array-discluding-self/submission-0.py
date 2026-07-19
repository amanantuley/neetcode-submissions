class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        ans = []

        pre = 1
        post = 1

        for i in range(len(nums)):
            ans[i] = pre
            pre = nums
            pre = nums[i] * pre

        for i in range(len(nums) -1 , -1 , -1):
            ans[i] = ans[i] * post
            post = post*nums[i]

        return ans