class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def flip(num, i, nums):

            for j in num:
                if j == 0:
                    nums[i] = 1
                else:
                    nums[i] = 0
                i += 1
            # print(num)
        
        res = 0
        for i in range(len(nums) - 2):

            if nums[i] == 0:
                flip(nums[i : i + 3], i, nums)
                # print(nums)
                res = res + 1
        if all(nums):
            return res
        else:
            return -1
