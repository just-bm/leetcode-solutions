class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stk = ['mn']

        for idx in logs:
            if idx == './':
                continue
            elif idx == '../' and len(stk) > 1:
                stk.pop()

            else:
                if idx[0] != '.':
                    stk.append(idx)
        return len(stk) - 1
