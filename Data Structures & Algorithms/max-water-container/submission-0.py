class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max = min(heights[left], heights[right]) * (right - left)
        while left < right:
            if min(heights[left], heights[right]) * (right - left) > max:
                max = min(heights[left], heights[right]) * (right - left)
            elif heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max