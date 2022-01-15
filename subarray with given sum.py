class Solution:
    def subArraySum(self,arr, n, s): 
        sums = 0
        start = 0
        ans = 0
        res = [0, 0]
        for i in range(n):
            sums += arr[i]
            while sums > s:
                sums -= arr[start]
                start = start+1
            if sums == s:
                if (i-start+1) > ans:
                    ans = i-start+1
                    res[0], res[1] = start+1, i+1
        return [-1] if res[0] == 0 and res[1] == 0 else res
