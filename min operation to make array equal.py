class Solution:
    def lcs(self, x, y, M, N):
        t = [[0 for _ in range(N+1)] for _ in range(M+1)]
        for m in range(1, M+1):
            for n in range(1, N+1):
                if x[m-1] == y[n-1]:
                    t[m][n] = t[m-1][n-1] + 1
                else:
                    t[m][n] = max(t[m][n-1], t[m-1][n])
        return t[M][N]
    
    def minInsAndDel(self, A, B, N, M):
        lcs = self.lcs(A, B, N, M)
        return N-lcs + M-lcs
