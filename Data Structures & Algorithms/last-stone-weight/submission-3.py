class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-i for i in stones]
        heapq.heapify(max_heap)
        
        while len(max_heap) > 1:
            largest = -heapq.heappop(max_heap)
            nxt_largest = -heapq.heappop(max_heap)
            if largest == nxt_largest:
                continue
            else:
                heapq.heappush(max_heap, -(largest-nxt_largest))
        if len(max_heap) == 0:
            return 0     
        return -heapq.heappop(max_heap)