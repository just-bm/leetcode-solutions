class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        d = {}
        count = 0
        for i in dominoes:
            i = tuple(sorted(i))
            d[i] = d.get(i, 0) + 1

        m = 0
        for key, val in d.items():
            m += val * (val - 1) // 2

        return m
