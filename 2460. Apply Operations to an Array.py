class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums) - 1
        i = 0
        while i < n:
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
            i += 1
        res = [0] * (n + 1)
        j = 0
        for i in range(n + 1):
            if nums[i] != 0:
                res[j] = nums[i]
                j += 1
        return res 
