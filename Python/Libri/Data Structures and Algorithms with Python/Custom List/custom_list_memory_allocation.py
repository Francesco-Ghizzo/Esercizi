class PyList:

    def __init__(self, numItems=0):

    # The growth pattern is:  0, 4, 8, 16, 25, 35, 46, 58, 72, 88, ...

        def new_allocated(oldsize):
            if oldsize < 8:
                new_size = oldsize + 4
            else:
                new_size = oldsize + 8 + (oldsize//8-1)
            return new_size
        
        allocated = 0
        
        if numItems > 0:
            while allocated < numItems:
                allocated = new_allocated(allocated)
                
        self.items = [None]*allocated
        self.numItems = numItems
        self.allocated = allocated


    # add this to iterate over all the values in the container:

    def __iter__(self):
        for item in self.items:
            yield item

    
    # add this to implement sequence assignment in your custom class:

    def __setitem__(self, key, value):
        self.items[key] = value

    
    # add this to implement retrieval of values in your custom class:

    def __getitem__(self, item):
        return self.items[item]

    
    # add this to implement printing your object:

    def __repr__(self) -> str:
        return f"{(self).items[:self.numItems]}"


    #add this to concatenate two custom lists:

    def __add__(self, other):
        result = self
        for i in other.items:
            result.append(i)
        return result
    
    # add this to implement append:

    def append(self, item):

        # The growth pattern is:  0, 4, 8, 16, 25, 35, 46, 58, 72, 88, ...

        def new_allocated(oldsize):
            if oldsize < 8:
                new_size = oldsize + 4
            else:
                new_size = oldsize + 8 + (oldsize//8-1)
            return new_size

        if self.numItems == self.allocated:
            self.allocated = new_allocated(self.allocated)
            newlst = [None]*self.allocated
            for i in range(self.numItems):
                newlst[i] = self.items[i]
            
            self.items = newlst

        self.items[self.numItems] = item
        self.numItems += 1
