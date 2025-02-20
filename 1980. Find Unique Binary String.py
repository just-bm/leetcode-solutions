class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = []
        n = len(nums)
        for i in range(2**n):
            s = bin(i)[2:].zfill(n)
            # print(s)
            res.append(s)
        for i in res:
            if i not in nums:
                return str(i)
