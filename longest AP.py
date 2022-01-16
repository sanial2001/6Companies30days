class Solution:
    def lengthOfLongestAP(self, A, n):
        if n == 1:
            return 1
        d = {}
        for i in range(n-1):
            for j in range(i+1, n):
                d[(j, A[j]-A[i])] = d.get((i, A[j]-A[i]), 1) + 1
        return max(d.values())
