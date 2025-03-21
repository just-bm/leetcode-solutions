class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        i = 0
        j = 2

        k = 1
        l = 3

        temp = [x for x in s1]
        some = [x for x in s2]
        x = temp[:]
        y = temp[:]

        x[i], x[j] = x[j], x[i]
        y[k], y[l] = y[l], y[k]
        z = x[:]
        a = x[:]
        z[l], z[k] = z[k], z[l]

         
        if temp == some:
            return True
        if (z) == some:
            return True
        elif (x) == some:
            return True
        elif (y) == some:
            return True
        else:
            return False
