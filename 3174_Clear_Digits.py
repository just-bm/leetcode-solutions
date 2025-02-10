class Solution:
    def clearDigits(self, s: str) -> str:
        stk = []
        n = len(s)
        for i in range(n):
            if s[i].isnumeric() and len(stk)>=1:
                stk.pop()
                continue
            else:
                stk.append(s[i])
            print(stk)
        res="".join(stk)
        return res

