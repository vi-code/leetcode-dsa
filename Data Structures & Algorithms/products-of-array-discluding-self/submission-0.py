class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_arr = [1] * len(nums)
        val = 1
        for index, num in enumerate(nums):    
            left_arr[index] = val
            val = val * num
        right_arr = [1] * len(nums)
        val = 1
        for index, num in reversed(list(enumerate(nums))):
            right_arr[index] = val
            val = val * num
        ans = [1] * len(nums)
        for i in range(len(right_arr)):
            ans[i] = (right_arr[i] * left_arr[i])
        return list(ans)