class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        mp = {}
        for i in nums1:
            x, y = i[0], i[1]
            mp[x] = y
        for j in nums2:
            x, y = j[0], j[1]
            mp[x] = mp.get(x, 0) + y
        x = sorted(mp)
        res = []
        for i in x:
            res.append([i, mp.get(i, 0)])
        return res
