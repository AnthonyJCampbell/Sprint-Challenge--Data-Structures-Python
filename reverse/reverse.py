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

        list_to_do = self.head.next_node
        
        reversed_list = self.head
        reversed_list.next_node = None

        while list_to_do is not None:
            temp = list_to_do
            list_to_do = list_to_do.next_node

            temp.next_node = reversed_list
            reversed_list = temp













        # current = self.head
        # # Loop over the length of the LinkedList
        # # Maybe a while loop, checking if self.head.next_node is not None
        # while True:
        #     # Call add_to_head on every value in the LinkedList
        #     print

        #     next = current.next_node

        #     # Store self.head
        #     stored_head = self.head

        #     # Run add_to_head
        #     self.add_to_head(current)

        #     # Do self.head.next_node = stored_head
        #     self.head.next_node = stored_head
            
        #     if next.next_node is None:
        #         break       
        #     else:     
        #         current = next

            


mylist = LinkedList()
mylist.add_to_head("1")
mylist.add_to_head("3")
mylist.add_to_head("2")
mylist.add_to_head("4")
mylist.reverse_list()
print(mylist.head.value)