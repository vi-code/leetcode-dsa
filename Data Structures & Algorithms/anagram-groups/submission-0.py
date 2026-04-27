class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = {}
        for word in strs:
            key = "".join(sorted(word))

            if key not in anagramMap:
                anagramMap[key] = []
            anagramMap[key].append(word)
        return list(anagramMap.values())