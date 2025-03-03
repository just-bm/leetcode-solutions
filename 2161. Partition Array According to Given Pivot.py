class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l = []
        r = []
        e = []
        for i in nums:
            if i < pivot:
                l.append(i)
            elif i==pivot:
                e.append(i)
            else:
                r.append(i)
        return l + e + r
