class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        temp = []

        for x in words:
            temp.append(x.lower())
        firstrow = set(['q','w','e','r','t','y','u','i','o',"p"])
        secondrow = set(['a','s','d','f','g','h','j','k','l'])
        thirdrow = set(['z','x','c','v','b','n','m'])
        res = []


        for word in range(len(words)):
            first = 0
            second = 0
            third = 0
            for letters in temp[word]:
                if letters in firstrow:
                    first += 1
                elif letters in secondrow:
                    second += 1
                elif letters in thirdrow:
                    third += 1

            if first > 0 and (second == 0 and third == 0):
                res.append(words[word])
            elif second > 0 and (first == 0 and third == 0):
                res.append(words[word])
            elif third > 0 and (second == 0 and first == 0):
                res.append(words[word])
        return res
