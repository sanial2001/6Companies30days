class Solution:
    def numSubarrayProductLessThanK(self, nums, k: int) -> int:
        start = 0
        prod, res = 1, 0
        for end in range(len(nums)):
            prod = prod*nums[end]
            while prod >= k:
                prod = prod//nums[start]
                start = start+1
            res = res + (end-start+1)
        return res


if __name__ == '__main__':
    print(Solution().numSubarrayProductLessThanK(nums = [10,5,2,6], k = 100))
