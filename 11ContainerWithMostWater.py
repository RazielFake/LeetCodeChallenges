#Problem 11 of LeetCode
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        maxHeight = 0
        width = len(height) - 1
        while left < right:
            maxHeight = max(maxHeight, (min(height[left], height[right])*width))
            width-=1
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
            
        return maxHeight
