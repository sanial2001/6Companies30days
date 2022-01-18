class Solution:
    def maxCoins(self,arr, n):
        t = [[-1 for _ in range(n)] for _ in range(n)]
        for g in range(n):
            i = 0
            for j in range(g, n):
                if g == 0:
                    t[i][j] = arr[i]
                elif g == 1:
                    t[i][j] = max(arr[i], arr[j])
                else:
                    t[i][j] = max(arr[i] + min(t[i+2][j], t[i+1][j-1]),
                                  arr[j] + min(t[i+1][j-1], t[i][j-2]))
                i = i+1
        for val in t:
            print(val)
        return t[0][n-1]
