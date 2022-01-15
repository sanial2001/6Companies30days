class Solution:
    def minSteps(self, D):
        # code here
        ans, k = 0, 0
        D = abs(D)
        while ans < D:
            ans += k
            k += 1
        while (ans-D)%2 == 1:
            ans += k
            k += 1
        return k-1
