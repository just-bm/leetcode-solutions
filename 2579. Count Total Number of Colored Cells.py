class Solution:
    def coloredCells(self, n: int) -> int:
        res = 1

        for i in range(n):
            res = res + 4 * i
        return res
