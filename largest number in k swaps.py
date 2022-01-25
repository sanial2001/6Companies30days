class Solution:

    # Function to find the largest number after k swaps.
    def solve(self, nums, index, k):
        if k == 0:
            self.ans = max(self.ans, int(''.join(nums)))
            return

        for i in range(index, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                    self.solve(nums, i, k - 1)

    def findMaximumNum(self, s, k):
        # code here
        s = list(s)
        self.ans = 0
        self.solve(s, 0, k)
        return str(self.ans)ka
