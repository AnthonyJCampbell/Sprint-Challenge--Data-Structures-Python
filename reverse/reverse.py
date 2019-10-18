class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None

    def add_to_head(self, value):
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)
        
        self.head = node

    def contains(self, value):
        if not self.head:
            return False
        # get a reference to the node we're currently at; update this as we traverse the list
        current = self.head
        # check to see if we're at a valid node 
        while current:
        # return True if the current value we're looking at matches our target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
            # if we've gotten here, then the target node isn't in our list
        return False

    def reverse_list(self):
        # if self.head is None or self.next_node is None, we can simply return
        if self.head is None or self.head.next_node is None:
            return

        current = self.head
        next = current.next_node

        # Loop over the list as long as there's a value to the right
        while next:
            # 'Remove' the value from the right
            # print(f"current node has a next_node of {current.next_node.value}. Changing it into {next.next_node.value}")
            current.next_node = next.next_node

            # The current value moves up a position
            # print(f"next.next_node (what used to be {next.next_node.value}) now becomes {self.head.value}")
            next.next_node = self.head

            # We're placing the value at head.next_node at head
            # print(f"We're now setting self.head (what used to be {self.head.value}) to {next.value}")
            self.head = next

            # Make next into current.next_node to reloop
            # print(f"Now, we're making sure next (what used to be {next.value} becomes current.next_node ({current.next_node.value}))")
            next = current.next_node

            # print("\n")
        return
