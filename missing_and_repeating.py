class Solution:
    def cycle(self, nums):
        i = 0
        while i < len(nums):
            if nums[i] == i+1 or nums[nums[i]-1] == nums[i]:
                i = i+1
            else:
                temp = nums[i]
                nums[i] = nums[temp-1]
                nums[temp-1] = temp
        return nums
    
    def findTwoElement( self,arr, n):
        nums = self.cycle(arr)
        ans = [-1 for _ in range(2)]
        for i in range(n):
            if nums[i] != i+1:
                ans[0] = nums[i]
                ans[1] = i+1
                break
        return ans
