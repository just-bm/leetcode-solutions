class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        seen = set()
        temp = set(nums)

        for i in nums:
            if i not in seen:
                seen.add(i)
            else:
                res.append(i)

        for j in range(1, n + 1):
            if j not in temp:
                res.append(j)

        return res
