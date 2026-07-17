class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        if len(nums) == k:
            return nums

        count = {}

        for i in nums:
            count[i] = count.get(i , 0) + 1

        sorted_nums = sorted(count , key=count.get , reverse=True)

        return sorted_nums[:k]