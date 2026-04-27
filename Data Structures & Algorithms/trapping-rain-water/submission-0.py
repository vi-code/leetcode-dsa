class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]
        ans = 0
        
        while left<right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                ans += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                ans += right_max - height[right]
        return ans
            
        # if not height:
        #     return 0

        # l, r = 0, len(height) - 1
        # leftMax, rightMax = height[l], height[r]
        # res = 0
        # while l < r:
        #     if leftMax < rightMax:
        #         l += 1
        #         leftMax = max(leftMax, height[l])
        #         res += leftMax - height[l]
        #     else:
        #         r -= 1
        #         rightMax = max(rightMax, height[r])
        #         res += rightMax - height[r]
        # return res