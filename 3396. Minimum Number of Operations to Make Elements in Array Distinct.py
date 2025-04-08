class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        freqCount = {}
        for i in nums:
            freqCount[i] = freqCount.get(i, 0) + 1
        flag = 0
        for key, value in freqCount.items():
            if value > 1:
                flag += 1
        count = 0
        if flag == 0:
            return flag
        else:
            while True:
                print(nums)
                if len(nums) >= 3:
                    nums.pop(0)
                    nums.pop(0)
                    nums.pop(0)
                    count += 1
                else:
                    del nums
                    count += 1
                    return count
                    
                mp = {}
                for i in nums:
                    mp[i] = mp.get(i, 0) + 1
                f = 0
                for k, v in mp.items():
                    if v > 1:
                        f += 1
                if f == 0:
                    return count
                    break

