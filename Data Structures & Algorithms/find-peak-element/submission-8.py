class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        n = nums.sort()
        max = 0
        for i in range(len(n)):
            for j in range(i+1 , len(n)):
                if n[i] > n[j]:
                    max = i
                elif n[i] < n[j]:
                    max = j
                
           
        return max