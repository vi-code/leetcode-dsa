class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left: int = 0
        right: int = len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left+1, right+1]
            if total > target:
                right -= 1
            elif total < target:
                left +=1
        return []