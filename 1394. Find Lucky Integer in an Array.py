class Solution:
    def findLucky(self, arr: List[int]) -> int:
        res = -1
        mp = dict()

        for i in arr:
            mp[i] = mp.get(i, 0) + 1

        for k in mp.keys():
            if k == mp[k]:
                res = max(res, k)

        return res
