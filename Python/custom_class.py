class PyList:

    def __init__(self, size=0):
        self.items = [None]*size

    def __iter__(self):
        for item in self.items:
            yield item

    def __repr__(self) -> str:
        return f"{(self).items}"
