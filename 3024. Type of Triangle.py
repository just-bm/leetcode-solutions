class Solution:
    def triangleType(self, nums: List[int]) -> str:
        test = set(nums)
        t = False
        a, b, c = nums[0], nums[1], nums[2]
        if a + b > c and a + c > b and b + c > a:
            t = True
        else:
            t = False
        if len(test) == 1 and t:
            return "equilateral"
        elif len(test) == 2 and t:
            return "isosceles"
        elif len(test) == 3 and t:
            return "scalene"
        else:
            return "none"
        
