class PyList:

    def __init__(self, size=0):
        self.items = [None]*size
        
    
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
        return f"{(self).items}"

    #add this to concatenate two custom lists:

    def __add__(self, other):
        result = self
        for i in other.items:
            result.append(i)
        return result

    # add this to implement append:

    def append(self, item):
        return self.items.append(item)
