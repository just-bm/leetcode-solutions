class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(x):
            low=0
            high=len(nums)

            while low<high:
                mid=(low+high)//2
                if nums[mid]<x:
                    low=mid+1
                else:
                    high=mid
            return low
        f=search(target)
        e=search(target+1)-1
        if f<=e:
            return [f,e]
        return [-1,-1]
