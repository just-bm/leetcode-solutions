class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def back(s, opencount, close, n, res):
            if len(s) == n * 2:
                res.append(s)

            if opencount < n:
                back(s + '(', opencount + 1, close, n, res)
            
            if close < opencount:
                back(s + ')', opencount, close + 1, n, res)
            
        res = []
        back("", 0, 0, n, res)
        return res
        

        
