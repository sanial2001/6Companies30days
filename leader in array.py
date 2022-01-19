class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        #Code here
        ans, max_till_now = [], -1
        for i in range(N-1, -1, -1):
            if A[i] > max_till_now:
                #print(A[i], max_till_now)
                ans.append(A[i])
                max_till_now = A[i]
        return ans[::-1]
