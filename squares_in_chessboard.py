class Solution:
    def squaresInChessBoard(self, N):
        ans = 0
        while N > 0:
            ans += N * N
            N = N - 1
        return ans
