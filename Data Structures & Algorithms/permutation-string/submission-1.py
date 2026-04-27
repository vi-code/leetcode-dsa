class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        desired: List[int] = [0] * 26
        window: List[int] = [0] * 26

        for i, c in enumerate(s1):
            desired[ord(c)-ord('a')] += 1
            window[ord(s2[i])-ord('a')] += 1

        matches: int = 0
        for i in range(len(desired)):
            if desired[i] == window[i]:
                matches+=1

        left: int = 0
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True
            right_idx = ord(s2[right]) - ord('a')
            left_idx = ord(s2[left]) - ord('a')
            window[right_idx] += 1
            compare_right = desired[right_idx] == window[right_idx]
            if compare_right:
                matches+=1
            elif desired[right_idx]+1 == window[right_idx]:
                matches-=1
            window[left_idx] -= 1
            compare_left = desired[left_idx] == window[left_idx]
            if compare_left:
                matches+=1
            elif desired[left_idx]-1 == window[left_idx]:
                matches-=1
            left+=1
            
        return matches == 26
