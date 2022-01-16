class Solution:
    def subset_sum(self, arr, s, n):
        if s == 0:
            return True
        elif n == 0:
            return False
        
        if arr[n-1] <= s:
            return subset_sum(arr, s-arr[n-1], n-1) or subset_sum(arr, s, n-1)
        else:
            return subset_sum(arr, s, n-1)
    
    def subset_sum_dp(self, arr, S, N):
        t = [[-1 for j in range(S+1)] for i in range(N+1)]
        
        for i in range(N+1):
            t[i][0] = True
        for i in range(1, S+1):
            t[0][i] = False
        
        for n in range(1, N+1):
            for s in range(1, S+1):
                if arr[n-1] <= s:
                    t[n][s] = t[n-1][s-arr[n-1]] or t[n-1][s]
                else:
                    t[n][s] = t[n-1][s]
        
        return t[N][S]

    
    def equalPartition(self, N, arr):
        # code here
        sum_ele = 0
        for val in arr:
            sum_ele = sum_ele + val
        
        if sum_ele % 2 == 0:
            return self.subset_sum_dp(arr, sum_ele//2, N)
        else:
            return False
