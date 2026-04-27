class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                ## start computing
                curr_bar = stack.pop()
                
                height = curr_bar[1]
                w = i - curr_bar[0]
                area = max(area, w*height)
                start = curr_bar[0]
                print(w, height, area)
            stack.append((start, h))
        while stack:
            curr_bar = stack.pop()
            c_start = curr_bar[0]
            height = curr_bar[1]
            w = len(heights) - c_start
            area = max(area, w*height)
        return area