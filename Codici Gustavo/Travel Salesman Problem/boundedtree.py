from threading import Semaphore

class BoundedTree(object):
    def __init__(self):
        self.l = []
        self.lock = Semaphore(1)

    def append(self, item, weight):
        with self.lock:
            pos = len(self.l)
            self.l.append((item, weight, 0, 0))
            while pos > 0:
                oldpos = pos
                pos -= 1
                pos >>= 1
                it, w1, wtl, wtr = self.l[pos]
                self.l[pos] = (it, w1, wtl + weight, wtr) if oldpos & 1 else (it, w1, wtl, wtr + weight)

    def __getindex(self, index):
        pos = soma = 0
        while pos < len(self.l):
            it, w1, wtl, wtr = self.l[pos]
            soma += w1
            if index < soma:
                return pos
            else:
                pos <<= 1
                if index < soma + wtl:
                    pos += 1
                else:
                    pos += 2
                    soma += wtl
        else:
            raise IndexError()
            
    def __popindex_aux(self, index, s1):
        while index > 0:
            oldindex = index
            index -= 1
            index >>= 1
            it_p, w1_p, wtl_p, wtr_p = self.l[index]
            self.l[index] = (it_p, w1_p, wtl_p + s1, wtr_p) if oldindex & 1 else (it_p, w1_p, wtl_p, wtr_p + s1)

    def __popindex(self, index):
        if index == len(self.l) - 1:
            it, w1, wtl, wtr = self.l.pop(index)
            self.__popindex_aux(index, -w1)
        else:
            it_n, w1_n = self.__popindex(len(self.l) - 1)
            it, w1, wtl, wtr = self.l[index]
            self.__popindex_aux(index, -w1)
            self.l[index] = (it_n, w1_n, wtl, wtr)
            self.__popindex_aux(index, w1_n)
        return (it, w1)

    def checktree(self, n=0):
        if n >= len(self.l):
            return 0
        it, w1, wtl, wtr = self.l[n]
        assert self.checktree((n << 1) + 1) == wtl and self.checktree((n << 1) + 2) == wtr
        return w1 + wtl + wtr

    def pop(self, x):
        with self.lock:
            index = self.__getindex(x)
            return self.__popindex(index)
