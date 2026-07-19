class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        output = []


        for i in range(len(nums) - 1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1 , len(nums) - 1):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left = j + 1
                right = len(nums) - 1

                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]
                    if s == target:
                        output.append([nums[i] , nums[j] , nums[left] , nums[right]])
                        left += 1
                        right -= 1
                    elif s < target:
                        left += 1
                    else :
                        right -= 1


                
        return output
                    

            
        