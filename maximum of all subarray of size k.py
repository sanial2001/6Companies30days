class Solution:
    
    #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self,arr,n,k):
        q = []
        res = []
        for i, num in enumerate(arr):
            while q and arr[i] > arr[q[-1]]:
                q.pop()
            q.append(i)
            if i == q[0] + k:
                q.pop(0)
            if i >= k-1:
                res.append(arr[q[0]])
        return res
        #code here
