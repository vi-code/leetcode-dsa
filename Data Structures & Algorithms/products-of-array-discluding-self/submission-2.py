class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        val = 1
        for index, num in enumerate(nums):    
            # left_arr[index] = val
            # val = val * num
            ans[index] = val
            val = val * num
        # right_arr = [1] * len(nums)
        val = 1
        print(ans)
        for index in range(len(nums)-1 , -1,-1):
            # right_arr[index] = val
            # val = val * num
            ans[index] = ans[index] * val
            val = val * nums[index]
        # ans = [1] * len(nums)
        # for i in range(len(right_arr)):
        #     ans[i] = (right_arr[i] * left_arr[i])
        return list(ans)