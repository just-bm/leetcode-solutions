class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count = 0
        for i in range(0, len(nums) - 2):
            j = i + 2
            if (nums[i] + nums[j]) * 2 == (nums[(i + j) // 2]): 
                count += 1
        return count
