class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s: set([int]) = set(nums)
        longest = 0
        
        for num in s:
            print("num:", num)
            length = 1
            if num-1 not in s:
                current_num = num
                while current_num+1 in s:
                    length += 1
                    current_num += 1
            longest = max(length, longest)
        return longest