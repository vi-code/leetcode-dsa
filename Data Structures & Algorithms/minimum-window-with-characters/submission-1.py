class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        t_count: dict[str, int] = {}
        for c in t:
            t_count[c] = t_count.get(c, 0) + 1
        
        left: int = 0
        have: int = 0
        need: int = len(t_count)
        best_len: float = float("inf")
        best_left = left
        best_right = left
        window_count: dict[str, int] = {}

        for right in range(len(s)):
            window_count[s[right]] = window_count.get(s[right], 0) + 1

            if s[right] in t_count and window_count[s[right]] == t_count[s[right]]:
                have += 1
            while have == need:
                curr = right - left + 1
                if curr < best_len:
                    # print(best_left, best_right, best_len)
                    best_right = right
                    best_left = left
                    best_len = curr
                window_count[s[left]] =  window_count.get(s[left],0) - 1
                
                if s[left] in t_count and window_count[s[left]] < t_count[s[left]]:
                    have -= 1
                left += 1
        if best_len == float("inf"):
            return ""

        return s[best_left: best_right+1]
                
                