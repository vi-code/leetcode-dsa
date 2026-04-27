class Solution:
    def binSearch(self, left: int, right: int, target: int, nums: List[int]) -> int:
        if left > right:
            return -1
        mid = (left+right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
            return self.binSearch(left, right, target, nums)
        elif nums[mid] > target:
            right = mid-1
            return self.binSearch(left, right, target, nums)

    def search(self, nums: List[int], target: int) -> int:
        return self.binSearch(0, len(nums)-1, target, nums)