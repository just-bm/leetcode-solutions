class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        q = []

        for i in range(low, high + 1):
            s = str(i)
            if len(s) % 2 == 0:
                first = s[:len(s) // 2]
                second = s[len(s) // 2 :]
                firstsum = 0
                secondsum = 0
                for f in first:
                    firstsum += int(f)
                for se in second:
                    secondsum += int(se)
                if firstsum == secondsum:
                    q.append(s)
        return len(q)
