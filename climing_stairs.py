    def dp(self, arr, M, N, mod):
        t = [[0 for _ in range(M+1)] for _ in range(N+1)]
        for i in range(N+1):
            t[i][0] = 1
        for n in range(1, N+1):
            for m in range(1, M+1):
                if arr[n-1] <= m:
                    t[n][m] = (t[n][m-arr[n-1]] + t[n-1][m])%mod
                else:
                    t[n][m] = t[n-1][m]%mod
        return t[N][M]
