class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                grid[0][j] = 1
                grid[i][0] = 1
        # for i in range(m):
        #     print(grid[i])
        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] == 0:
                    grid[i][j] += grid[i - 1][j] + grid[i][j - 1]
        return grid[m - 1][n - 1]
