class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sol = 0
        for i in nums:
            sol = sol ^ i
        return sol
