class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    # When the ring buffer is full and a new element is inserted, 
    # the oldest element in the ring buffer is overwritten with the newest element. 
    def append(self, item):

        print(f"inserting {item} at [{self.current}]")
        self.storage[self.current] = item

        self.current += 1

        if self.current > len(self.storage) - 1:
            self.current = 0

    #  The `get` method returns all of the elements in the buffer in a list in their given order. 
    # It should not return any `None` values in the list even if they are present in the ring buffer.
    def get(self):
        # Declare output list
        output = []

        for item in self.storage:
            if item is not None:
                output.append(item)

        return output

# buffer = RingBuffer(5)
# buffer.append('a')
# buffer.append('b')
# buffer.append('c')
# buffer.append('d')
# buffer.append('e')
# buffer.append('f')
# print(buffer.get())