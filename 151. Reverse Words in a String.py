class Solution:
    def reverseWords(self, s: str) -> str:
        res = list(map(str, s.split()))
         
        return " ".join(res[::-1])
