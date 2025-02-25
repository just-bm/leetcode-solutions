class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        count = 0
        n = len(arr)
        res  = 0
        odd = 0
        even = 0
        mod = 10**9 + 7
        for idx in arr:
            res += idx
            if res % 2 != 0:
                count += 1
                count += even
                count %= mod
                odd += 1
            else:
                count += odd
                count %= mod 
                even += 1
        return count

