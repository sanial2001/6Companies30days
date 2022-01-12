class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        while matrix:
            m = list(matrix.pop(0))
            for val in m:
                ans.append(val)
            matrix[:] = zip(*matrix)
            matrix = matrix[::-1]
        '''
        res = []
        for val in ans:
            for i in val:
                res.append(i)
        return res
        '''
        return ans
