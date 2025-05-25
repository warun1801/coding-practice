class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        queue = []
        dom = list(dominoes)
        for i, val in enumerate(dom):
            if val in ('L', 'R'):
                queue.append((val, i))

        temp = [i for i in dom]
        while queue:
            val, i = queue.pop(0)
            if val == 'L':
                if i != 0:
                    if temp[i - 1] not in ('L', 'R'):
                        if temp[i - 1] == '.':
                            temp[i - 1] = 0
                        temp[i - 1] -= 1
            else:
                if i != len(temp) - 1:
                    if temp[i + 1] not in ('L', 'R'):
                        if temp[i + 1] == '.':
                            temp[i + 1] = 0
                        temp[i + 1] += 1
            if not queue:
                for i in range(len(temp)):
                    if temp[i] not in ('L', 'R', '.'):
                        val = 'L' if temp[i] < 0 else 'R' if temp[i] > 0 else '.'
                        if val in ('L', 'R'):
                            queue.append((val, i))

        return temp 


                                                        

