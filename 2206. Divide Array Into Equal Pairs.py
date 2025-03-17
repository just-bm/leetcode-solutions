class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        mp = {}

        for i in nums:
            mp[i] = mp.get(i, 0) + 1
        for key, val in mp.items():
            if val % 2 != 0:
                return False
        return True
