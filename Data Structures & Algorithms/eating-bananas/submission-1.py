class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        
        while left <= right:
            mid = (right + left) // 2
            total_hours = 0
            for i in range(len(piles)):
                total_for_1 = (piles[i] + mid - 1) // mid ## Ceil replacement
                total_hours += total_for_1
            if total_hours > h:
                left = mid + 1
            else:
                right = mid - 1

        return left
