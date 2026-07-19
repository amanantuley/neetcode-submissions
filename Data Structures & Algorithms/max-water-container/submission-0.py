class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        res = 0
        for i in range(len(heights)):
            for j in range(i + 1 , len(heights)):
                res = max(res , min(height[i] , height[j]) * (j - i))

        return res