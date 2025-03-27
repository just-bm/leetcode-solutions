class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        s = set()

        mp = dict()

        for i in arr:
            mp[i] = mp.get(i, 0) + 1
        
        for key, val in mp.items():
            if val in s:
                return False
            s.add(val)
        return True
