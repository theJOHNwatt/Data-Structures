"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next
        # ADD IN A KEY

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, key, value):
        new_node = ListNode(key, value, None, None)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head 
            self.head.prev = new_node
            self.head = new_node 

    def remove_from_head(self):
        key = self.head.key
        value = self.head.value 

        if self.head is None: 
            return None
        self.delete(self.head)
        return key,value


    def add_to_tail(self, key, value):
        new_node = ListNode(key, value, None, None)
        self.length += 1
        if not self.head and not self.tail:
            self.head = self.tail = ListNode(key, value, None, None)
        else:
            new_node.prev = self.tail 
            self.tail.next = new_node
            self.tail = new_node

    def remove_from_tail(self):
        key = self.tail.key 
        value = self.tail.value 
        if self.tail is None:
            return None 
        self.delete(self.tail)
        return key,value

    def move_to_front(self, node):
        # key = node.key 
        # value = node.value 

        if node is self.head:
            return
        key = node.key 
        value = node.value 
        self.delete(node)
        self.add_to_head(key, value)

    def move_to_end(self, node):
        key = node.key 
        value = node.value 
        if node is self.tail:
            return value
        self.delete(node)
        self.add_to_tail(key, value)

    def delete(self, node):
        self.length -= 1
        if not self.head and not self.tail:
            print("ERROR: Attempted to delete node not in list")
            return 
        if self.head == self.tail: 
            self.head == None 
            self.tail == None 
        # elif self.head == node:
        elif node == self.head:
            # self.head = self.head.next 
            self.head = node.next
            node.delete()
        # elif self.tail == node:
        elif node == self.tail:
            # self.tail = self.tail.prev
            self.tail = node.prev
            node.delete()
        else:
            node.delete() 



    def get_max(self):
        current_node = self.head 
        # MISTAKE HERE - NOT self.head.value // SUPPOSE TO BE current_node.value
        max_value = current_node.value 
        while current_node is not None:
            if current_node.value > max_value:
                max_value = current_node.value 
            current_node = current_node.next