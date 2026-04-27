class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left: int = 0
        longest: int = 0
        seen = {}

        for right, char in enumerate(s):
            print(left, right, char, seen)
            if char in seen:
                left = max(left, seen[char]+1)
            seen[char] = right
            window = right-left+1
            print(longest, window)
            longest = max(longest, window)
        return longest