class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sums = 0
        start = 0
        ans = 100000000
        for i in range(len(nums)):
            sums += nums[i]
            while sums >= target:
                ans = min(ans, i-start+1)
                sums = sums-nums[start]
                start = start+1
        return 0 if ans == 100000000 else ans
