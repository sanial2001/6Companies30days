class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a, b = 0, 0
        n = len(colors)
        for i in range(1, n-1):
            if colors[i-1] == colors[i] == colors[i+1]:
                if colors[i] == 'A':
                    a += 1
                else:
                    b += 1
        return a > b
