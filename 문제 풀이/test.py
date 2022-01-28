class binaryheap(object):
    def __init__(self):
        self.items = [None]

    def __len__(self):
        return len(self.items) -1
    
    def _up_(self):
        i = len(self)
        parent = i//2
        while parent > 0:
            if self.items[i] < self.items[parent]:
                self.items[i], self.items[parent] = self.items[parent], self.items[i]
            i = parent
            parent = i//2
    
    def push(self, val):
        self.items.append(val)
        self._up_()
    
    def _down_(self, idx):
        left, right = idx*2, idx*2 +1
        small = idx
        
        if left <= len(self) and self.items[left] < self.items[small]:
            small = left
        if right <= len(self) and self.items[right] < self.items[right]:
            small = right
        if small != idx:
            self.items[idx], self.items[small] = self.items[small], self.items[idx]
            self._down_(small)
    
    def pop(self):
        self.items[1] = self.items[-1]
        ret = self.items.pop()
        self._down_(1)
        return ret