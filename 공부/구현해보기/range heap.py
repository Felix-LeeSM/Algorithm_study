
class RangeHeap(list):
    def __init__(self):
        self.size = 0
        super().__init__()

    def push(self, x):
        self.size += 1
        if self.size == 1:
            self.append(x)
            return

        if self.size == 2:
            cur = self[0]
            self[0] = (min(cur, x), max(cur, x))
            return

        if self.size % 2:
            self.append(x)
            idx = len(self)-1

            parent = (idx-1) >> 1

            parMin, parMax = self[parent]
            if parMin <= x <= parMax:
                return
            if x < parMin:
                self[parent] = (x, parMax)
                self[idx] = parMin
            else:
                self[parent] = (parMin, x)
                self[idx] = parMax

            idx = parent

            while idx > 0:
                parent = (idx-1) >> 1

                curMin, curMax = self[idx]
                parMin, parMax = self[parent]
                if curMin <= parMin and curMax >= parMax:
                    return

                self[parent] = (min(curMin, parMin), max(curMax, parMax))
                self[idx] = (max(curMin, parMin), min(curMax, parMax))

                idx = parent

            return

        idx = len(self)-1
        cur = self[-1]
        if x < cur:
            self[-1] = (x, cur)
        else:
            self[-1] = (cur, x)

        while idx > 0:
            parent = (idx-1) >> 1

            curMin, curMax = self[idx]
            parMin, parMax = self[parent]
            if curMin <= parMin and curMax >= parMax:
                return

            self[parent] = (min(curMin, parMin), max(curMax, parMax))
            self[idx] = (max(curMin, parMin), min(curMax, parMax))

            idx = parent

    def popMax(self):
        if not self.size:
            raise IndexError('pop from empty heap')
        if self.size == 1:
            self.size -= 1
            return self.pop()
        if self.size == 2:
            self.size -= 1
            curMin, curMax = self.pop()
            self.append(curMin)
            return curMax

        idx = 0

        if self.size % 2:
            self.size -= 1
            totMin, totMax = self[idx]
            x = self.pop()

            if totMin < x:
                self[idx] = (totMin, x)
            else:
                self[idx] = (x, totMin)

            while idx:
                lIdx, rIdx = (idx << 1) + 1, (idx << 1) + 2
                if lIdx >= len(self):
                    break
                next_ = lIdx
                if rIdx < len(self) and (self[rIdx][0] < self[lIdx][0] or self[rIdx][1] > self[lIdx][1]):
                    next_ = rIdx

                curMin, curMax = self[idx]
                nxtMin, nxtMax = self[next_]

                self[idx] = (min(curMin, nxtMin), max(curMax, nxtMax))
                self[next_] = (max(curMin, nxtMin), min(curMax, nxtMax))
                idx >>= 1

            return totMax

        self.size -= 1
        totMin, totMax = self[idx]
        tailMin, tailMax = self[-1]
        self[idx] = (totMin, tailMax)
        self[-1] = tailMin

        while idx < len(self):
            lIdx, rIdx = (idx << 1) + 1, (idx << 1) + 2
            if lIdx >= len(self):
                break
            if type(self[lIdx]) == int:
                a, b = self[idx]
                c = self[lIdx]
                a, b, c = sorted([a, b, c])
                self[idx] = (a, c)
                self[lIdx] = b
                break

            next_ = lIdx
            if rIdx < len(self):
                if type(self[rIdx]) == int:
                    a, b = self[idx]
                    c = self[rIdx]
                    a, b, c = sorted([a, b, c])
                    self[idx] = (a, c)
                    self[rIdx] = (b)
                    break
                if self[rIdx][0] < self[lIdx][0] or self[rIdx][1] > self[lIdx][1]:
                    next_ = rIdx

            curMin, curMax = self[idx]
            nxtMin, nxtMax = self[next_]
            if curMin <= nxtMin and curMax >= nxtMax:
                break

            self[idx] = (min(curMin, nxtMin), max(curMax, nxtMax))
            self[next_] = (max(curMin, nxtMin), min(curMax, nxtMax))
            idx = next_

        return totMax

    def popMin(self):
        if not self.size:
            raise IndexError('pop from empty heap')
        if self.size == 1:
            self.size -= 1
            return self.pop()
        if self.size == 2:
            self.size -= 1
            totMin, totMax = self[0]
            self[0] = totMax
            return totMin

        if self.size % 2:
            idx = 0
            self.size -= 1
            totMin, totMax = self[idx]
            tail = self.pop()
            self[idx] = (tail, totMax)

            while idx < len(self):
                lIdx, rIdx = (idx << 1) + 1, (idx << 1) + 2
                if lIdx >= len(self):
                    break
                next_ = lIdx
                if rIdx < len(self) and (self[rIdx][0] < self[lIdx][0] or self[rIdx][1] > self[lIdx][1]):
                    next_ = rIdx

                curMin, curMax = self[idx]
                nxtMin, nxtMax = self[next_]
                if curMin <= nxtMin and curMax >= nxtMax:
                    break

                self[idx] = (min(curMin, nxtMin), max(curMax, nxtMax))
                self[next_] = (max(curMin, nxtMin), min(curMax, nxtMax))
                idx = next_

            return totMin

        idx = 0
        self.size -= 1
        totMin, totMax = self[idx]
        tailMin, tailMax = self[-1]
        self[idx] = (tailMin, totMax)
        self[-1] = tailMax

        while idx < len(self):
            lIdx, rIdx = (idx << 1) + 1, (idx << 1) + 2

            if lIdx >= len(self):
                break
            if type(self[lIdx]) == int:
                a, b = self[idx]
                c = self[lIdx]
                a, b, c = sorted(a, b, c)
                self[idx] = (a, c)
                self[lIdx] = b
                break

            next_ = lIdx

            if rIdx < len(self):
                if type(self[rIdx]) == int:
                    a, b = self[idx]
                    c = self[rIdx][0]
                    a, b, c = sorted(a, b, c)
                    self[idx] = (a, c)
                    self[rIdx] = b
                    break
                if self[rIdx][0] < self[lIdx][0] or self[rIdx][1] > self[lIdx][1]:
                    next_ = rIdx

            curMin, curMax = self[idx]
            nxtMin, nxtMax = self[next_]
            if curMin <= nxtMin and curMax >= nxtMax:
                break
            self[idx] = (min(curMin, nxtMin), max(curMax, nxtMax))
            self[next_] = (max(curMin, nxtMin), min(curMax, nxtMax))
            idx = next_

        return totMin
