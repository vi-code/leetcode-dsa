class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i,j=0,len(nums)
        if len(nums) == 1 and target != nums[i]:
            return -1
        elif len(nums) == 1 and target == nums[i]:
            return 0
        while j-i > 1:
            if target == nums[i]:
                return i
            print(i,j)
            mid = int((j + i)/2)
            print(int(mid))
            if target > nums[mid]:
                i = mid
            elif target < nums[mid]:
                j = mid
            elif target == nums[mid]:
                return mid
        return -1
            