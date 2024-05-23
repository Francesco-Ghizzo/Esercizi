class PyList:

    def __init__(self, size=0):
        self.items = [None]*size

    def __iter__(self):
        for item in self.items:
            yield item

    def __repr__(self) -> str:
        return f"{(self).items}"


    def list_resize(oldsize):
        if oldsize < 8:
            new_allocated = oldsize + 4
        else:
            new_allocated = oldsize + 8 + (oldsize//8-1)
        return new_allocated