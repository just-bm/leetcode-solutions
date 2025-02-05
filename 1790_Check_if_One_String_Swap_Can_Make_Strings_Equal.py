class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        n = len(s1)

        stk = []
        for i in range(n):
            if s1[i] != s2[i]:
                stk.append(i)
            if len(stk) > 2:
                return False
        
        if len(stk) == 2:
            if s1[stk[0]] == s2[stk[1]] and s1[stk[1]] == s2[stk[0]]:
                return True

        return False
