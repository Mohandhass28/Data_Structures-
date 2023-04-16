class heap:
    def __init__(self,max):
        self.maxsize = max
        self.heap = []
        self.size = 0
        self.front = 1
        self.heap = [0] * self.maxsize

    def parent(self,pos):
        return pos // 2

    def leftchilde(self,pos):
        return pos * 2

    def rightchild(self,pos):
        return pos * 2 + 1

    def isleaf(self,pos):
        return pos * 2 > self.size

    def swap(self,fpos,spos):
        self.heap[fpos],self.heap[spos] = self.heap[spos],self.heap[fpos]

    def inserte(self,val):
        if self.size >=self.maxsize:
            return
        self.size += 1
        self.heap[self.size] = val
        current = self.size
        while self.heap[current] < self.heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)
    def delete(self):
        if self.size == 0:
            return
        pop = self.heap[self.front]
        self.heap[self.front] = self.heap[self.size]
        self.size -= 1
        self.heapfipy(self.front)
        return pop


    def heapfipy(self,front):
        if not self.isleaf(front):
            if self.heap[front] > self.heap[self.leftchilde(front)] or self.heap[front] > self.heap[self.rightchild(front)]:
                if self.heap[self.leftchilde(front)] < self.heap[self.rightchild(front)]:
                    self.swap(front,self.leftchilde(front))
                    self.heapfipy(self.leftchilde(front))
                else:
                    self.swap(front,self.rightchild(front))
                    self.heapfipy(self.rightchild(front))


he = heap(9)
he.inserte(5)
he.inserte(4)
he.inserte(2)
he.inserte(8)
he.inserte(21)
he.inserte(9)

