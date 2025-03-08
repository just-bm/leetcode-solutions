class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        i = 0
        res = 99999999999999999999999999999
        while i + k <= len(blocks):
            x = blocks[i: i + k]
            count = 0
            for char in x:
                if char == 'W':
                    count += 1
            # print(x)
            res = min(res, count)
            # print(x)
            i += 1
        return res
