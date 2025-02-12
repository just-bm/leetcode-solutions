class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i,j=0,0
        m,n=len(s),len(t)

        while i<m and j<n:
            if s[i]==t[j]:
                i+=1
            j+=1
        return i==m
