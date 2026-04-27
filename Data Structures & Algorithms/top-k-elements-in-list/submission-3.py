class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for i, num in enumerate(nums):
            hm[num] = hm.get(num,0) + 1
        # sorted_hm = dict(sorted(hm.items(), key=lambda item: item[1], reverse=True))
        # ans = []
        print(hm)
        # for key,val in sorted_hm.items():
        #     if k == 0: 
        #         return ans
        #     ans.append(key)
        #     k -= 1
        # return ans
        bucket: List[List[int]] = [[] for _ in range(len(nums)+1)]
        answer = []
        for key,val in hm.items():
            bucket[val].append(key)
        print(bucket)
        for freq in range(len(bucket)-1, 0, -1):
            for val in bucket[freq]:
                answer.append(val)
                if len(answer) == k:
                    return answer
        return answer