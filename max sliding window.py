class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = []
        out = []
        for i, n in enumerate(nums):
            while d and nums[d[-1]] < n:
                d.pop()
            d.append(i)
            if d[0] == i - k:
                d.pop(0)
            if i >= k - 1:
                out += nums[d[0]],
        return out
