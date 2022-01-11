class Solution:
    def subset_sum(self, arr, S, N):
        t = [[0 for _ in range(S+1)] for _ in range(N+1)]
        
        for i in range(N+1):
            t[i][0] = 1
        
        for n in range(1, N+1):
            for s in range(1, S+1):
                if arr[n-1] <= s:
                    t[n][s] = t[n-1][s-arr[n-1]] or t[n-1][s]
                else:
                    t[n][s] = t[n-1][s]
        
        vec = []
        if S % 2 != 0:
            for i in range((S+1) // 2):
                if t[N][i]:
                    vec.append(i)
        else:
            for i in range((S+1)//2 + 1):
                if t[N][i]:
                    vec.append(i)
        
        return vec
        
	def minDifference(self, nums, n):
		# code here
        sums = sum(nums)
        vec = self.subset_sum(nums, sums, len(nums))
        ans = 10000000000
        for i in vec:
            ans = min(ans, sums-2*i)
        return ans
