class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        mp = {}
        n = len(nums)
        count = 0
        for i in range(n):
            mp[nums[i]-i] = mp.get(nums[i]-i, 0) + 1
        for key, val in mp.items():
            if val >= 1:
                count += key*(key-1)/2

        return int(n*(n-1)/2 - count)
