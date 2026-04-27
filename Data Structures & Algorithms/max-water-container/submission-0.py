class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best_area: int = 0
        left: int = 0
        right: int = len(heights)-1
        while left < right:
            area = (right-left)*(min(heights[right],heights[left]))
            best_area = max(area, best_area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return best_area