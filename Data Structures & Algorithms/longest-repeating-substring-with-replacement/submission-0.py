class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left: int = 0
        right: int = 0
        max_freq: int = 0
        best: int = 0
        counts: dict[str, int] = {}

        for right, char in enumerate(s):
            print(counts)
            counts[char] = counts.get(char, 0) + 1
            max_freq = max(max_freq, counts[char])

            window_size = right-left+1
            replacements_needed = window_size - max_freq
            if replacements_needed > k:
                counts[s[left]] -= 1
                left += 1
            best = max(best, right-left+1)   
        return best