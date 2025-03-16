class Solution:
    def maxSum(self, nums: List[int]) -> int:
        nums = list(set(nums))
        greater = []
        lesser = []

        for i in nums:
            if i <= 0:
                lesser.append(i)
            else:
                greater.append(i)
        if sum(greater) == 0:
            return max(lesser)
        else:
            return sum(greater)
