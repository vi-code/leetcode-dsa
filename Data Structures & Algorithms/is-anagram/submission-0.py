class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = [0] * 26
        for char1, char2 in zip(s,t):
            index1 = ord(char1) - ord('a')
            counter[index1] += 1
            index2 = ord(char2) - ord('a')
            counter[index2] -= 1
        return all(x == 0 for x in counter)
