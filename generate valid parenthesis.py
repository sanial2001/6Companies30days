class Solution:
    def solve(self, ip, op, path, ans):
        if ip == 0 and op == 0:
            ans.append(path[::])
            return
        if ip != 0:
            self.solve(ip-1, op, path+'(', ans)
        if ip < op:
            self.solve(ip, op-1, path+')', ans)
            
    def AllParenthesis(self,n):
        ans = []
        self.solve(n, n, '', ans)
        return ans
