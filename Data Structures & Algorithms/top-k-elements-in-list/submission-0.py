class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for i, num in enumerate(nums):
            if hm.get(num) is None:
                hm[num] = 0
            else:
                hm[num] = hm[num] + 1
        sorted_hm = dict(sorted(hm.items(), key=lambda item: item[1], reverse=True))
        ans = []
        print(sorted_hm)
        for key,val in sorted_hm.items():
            if k is 0: 
                return ans
            ans.append(key)
            k -= 1
        return ans
        