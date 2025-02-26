class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(indices)
        h = [0] * (n)
        for i in range(n):
            h[indices[i]] = s[i]
        return "".join(h)
