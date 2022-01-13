class Solution:
    
    #Function to calculate the span of stockâ€™s price for all n days.
    def calculateSpan(self,a,n):
        #code here
        stack, index, res = [], [], []
        for i in range(n):
            if len(stack) == 0:
                res.append(1)
            elif len(stack) > 0 and stack[-1] < a[i]:
                res.append(i-index[-1]+1)
            elif len(stack) > 0 and stack[-1] >= a[i]:
                stack.pop()
                index.pop()
                while stack and stack[-1] >= a[i]:
                    stack.pop()
                    index.pop()
                if len(stack) == 0:
                    res.append(1)
                elif len(stack) > 0 and stack[-1] < a[i]:
                    res.append(i-index[-1]+1)
            stack.append(a[i])
            index.append(i)
        return res
