class PyList:

    def __init__(self, size=0):
        self.items = [None]*size

    def __iter__(self):
        for item in self.items:
            yield item

    def __repr__(self) -> str:
        return f"{(self).items}"


    def inefficientAppend(self, item):
        self.items = self.items + [item]

   # The growth pattern is:  0, 4, 8, 16, 25, 35, 46, 58, 72, 88, ...

    def new_allocated(oldsize):
        if oldsize < 8:
            new_size = oldsize + 4
        else:
            new_size = oldsize + 8 + (oldsize//8-1)
        return new_size