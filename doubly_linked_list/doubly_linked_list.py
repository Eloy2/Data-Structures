"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value): # DONE
        if (self.head == None) and (self.tail == None):
            new_node = ListNode(value, None, None)
            self.head = new_node
            self.tail = new_node
            self.length = self.length + 1
        else:
            new_node = ListNode(value, None, None)
            current_head = self.head
            current_head.prev = new_node
            new_node.next = current_head
            self.head = new_node
            self.length = self.length + 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self): # DONE
        if self.head == self.tail:
            current_head = self.head
            self.head = None
            self.tail = None
            self.length = self.length - 1
            return current_head.value
        else:
            current_head = self.head
            node_after_head = current_head.next
            node_after_head.prev = None
            current_head.prev = None
            current_head.next = None
            self.head = node_after_head
            self.length = self.length - 1
            return current_head.value
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value): # DONE
        if (self.head == None) and (self.tail == None):
            new_node = ListNode(value, None, None)
            self.head = new_node
            self.tail = new_node
            self.length = self.length + 1
        else:
            new_node = ListNode(value, None, None)
            current_tail = self.tail
            current_tail.next = new_node
            new_node.prev = current_tail
            self.tail = new_node
            self.length = self.length + 1

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self): # DONE
        if self.head == self.tail:
            current_tail = self.tail
            self.head = None
            self.tail = None
            self.length = self.length - 1
            return current_tail.value
        else:
            current_tail = self.tail
            node_before_tail = current_tail.prev
            node_before_tail.next = None
            current_tail.next = None
            current_tail.prev = None
            self.tail = node_before_tail
            self.length = self.length - 1
            return current_tail.value

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node): # DONE
        if self.head == self.tail:
            return None
        elif self.head == node:
            return None
        else:
            prev_node = node.prev # GET previous node
            next_node = node.next # GET next node
            if prev_node == None: # ASSUME it's the head
                next_node.prev = None
                self.head = next_node
                node.next = None
            elif next_node == None: # ASSUME it's the tail
                prev_node.next = None
                self.tail = prev_node
                node.prev = None
            else:
                prev_node.next = next_node # SET prev_node.next equal to next_node
                next_node.prev = prev_node # SET next_node.prev equal to prev_node

            current_head = self.head # GET current head
            current_head.prev = node # SET current_head.prev equal to 
            node.next = current_head # SET node.next equal to current_head
            node.prev = None # SET node.prev equal to None
            self.head = node # SET the head of list equal to node

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node): # DONE
        if self.head == self.tail:
            return None
        elif self.tail == node:
            return None
        else:
            prev_node = node.prev # GET previous node
            next_node = node.next # GET next node
            if prev_node == None: # ASSUME it's the head
                next_node.prev = None
                self.head = next_node
                node.next = None
            elif next_node == None: # ASSUME it's the tail
                prev_node.next = None
                self.tail = prev_node
                node.prev = None
            else:
                prev_node.next = next_node # SET prev_node.next equal to next_node
                next_node.prev = prev_node # SET next_node.prev equal to prev_node

            current_tail = self.tail # GET the current tail
            current_tail.next = node # SET current_tail.next equal to node
            node.prev = current_tail # SET node.previous equal to current_tail 
            node.next = None # SET node.next equal to None
            self.tail = node # SET the tail of list equal to node

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node): # DONE
        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.length = self.length - 1
            return node
        elif (self.head == None) and (self.tail == None):
            return None
        else:
            prev_node = node.prev # GET previous node
            next_node = node.next # GET next node
            if prev_node == None: # ASSUME the node that we will delete is the head
                self.head = next_node
                next_node.prev = None
                node.next = None
                self.length = self.length - 1
                return node.value
            elif next_node == None: # ASSUME the node that we will delete is the tail
                self.tail = prev_node
                prev_node.next = None
                node.prev = None
                self.length = self.length - 1
                return node.value
            else:
                prev_node.next = next_node # SET prev_node.next equal to next_node
                next_node.prev = prev_node # SET next_node.prev equal to prev_node
                self.length = self.length - 1
                node.prev = None
                node.next = None
                return node.value

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self): # DONE
        # If length == 0 return None
        if self.length == 0:
            return None
        # If length == 1 return self.head.value
        if self.length == 1:
            return self.head.value
        # Current_max starts out as self.head.value
        current_max = self.head.value
        # Iterate through the list
        current_node = self.head
        # Stop when current_node is None
        while current_node is not None:
        # Compare current_max to each value and update current_max if value > current_max
            if current_max < current_node.value:
                current_max = current_node.value
        # Move current_node forward
            current_node = current_node.next
        # Return current_max
        return current_max

    def display_list(self):
        if self.head is None:
            print("List has no Nodes")
        else:
            current_node = self.head
            while current_node is not None:
                print(current_node.value, "->")
                current_node = current_node.next
