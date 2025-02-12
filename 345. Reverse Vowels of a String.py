class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel=[]
        check=['a','e','i','o','u','A','E','I','O','U']
        for i in s:
            if i in check:
                vowel.append(i)
        
        res=""
        
        for i in s:
            if i in check and len(vowel)>0:
                # print(res)
                res+=vowel.pop()
                continue
            res+=i
        return res
