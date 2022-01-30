class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        pq = []
        for num in nums:
            heapq.heappush(pq, int(num)*-1)
        while k > 0:
            res = heapq.heappop(pq)
            if k == 1:
                return str(res*-1)
            k = k-1
