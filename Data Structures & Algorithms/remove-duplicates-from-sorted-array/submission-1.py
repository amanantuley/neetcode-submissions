class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:


        hashset = set()
        for i in range(len(nums)):
            hashset.add(i)

        return list(hashset)

        
    