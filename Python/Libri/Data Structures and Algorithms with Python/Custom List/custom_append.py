class PyList:

    def __init__(self, numItems=0):
        allocated = 0
        if numItems > 0:
            while allocated < numItems:
                allocated = new_allocated(allocated)
        self.items = [None]*allocated
        self.numItems = numItems
        self.allocated = allocated
        
        
   # The growth pattern is:  0, 4, 8, 16, 25, 35, 46, 58, 72, 88, ...

    def new_allocated(oldsize):
        if oldsize < 8:
            new_size = oldsize + 4
        else:
            new_size = oldsize + 8 + (oldsize//8-1)
        return new_size

    def __iter__(self):
        for item in self.items:
            yield item

    # add this to implement printing your object:

    def __repr__(self) -> str:
        return f"{(self).items}"

    # add this to implement sequence assignment in your custom class:

    def __setitem__(self, key, value):
        self.items[key] = value

    def __getitem__(self, item):
        return self.items[item]


    # custom append methods

    def inefficientAppend(self, item):
        self.items = self.items + [item]


    def efficientAppend(self, item):

        if self.numItems == self.allocated:
            self.allocated = new_allocated(self.allocated)
            newlst = [None]*self.allocated
            for i in range(self.numItems):
                newlst[i] = self.items[i]
            
            self.items = newlst

        self.items[self.numItems] = item
        self.numItems += 1
