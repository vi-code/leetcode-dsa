class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # length = len(nums)
        # for i in range(length):
        #     for j in range(length):
        #         if i != j and nums[i] == nums[j]:
        #             return True
        
        # return False
        remove_dups = set(nums)
        if len(remove_dups) != len(nums):
            return True
        return False