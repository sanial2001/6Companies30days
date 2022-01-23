class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        N = len(grid)
        new_grid = [[] for _ in range(N)]
        for i in range(N):
            for j in range(N):
                new_grid[i].append(Node(grid[i][j] == 1, True, None, None, None, None))
        while N > 0:
            N //= 2
            for i in range(N):
                for j in range(N):
                    a = new_grid[i * 2][j * 2]
                    b = new_grid[i * 2][j * 2 + 1]
                    c = new_grid[i * 2 + 1][j * 2]
                    d = new_grid[i * 2 + 1][j * 2 + 1]
                    if a.val == b.val == c.val == d.val and a.val != '*':
                        new_grid[i][j] = Node(a.val, True, None, None, None, None)
                    else:
                        new_grid[i][j] = Node('*', False, a, b, c, d)
        return new_grid[0][0]
