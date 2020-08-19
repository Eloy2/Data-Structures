# import sys
# # sys.path.insert(0, 'C:/Users/Eloy D. Gutierrez/Data-Structures/singly_linked_list')
from singly_linked_list import LinkedList
"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?

   An array is a built in data structure. So we can use the built it methods to easily implement the Stack. 
   When using a Linked list the storage attribute is an instance of our Linked list class. We would then use the methods that our
   instance has to implement our Stack. A ran into a problem when trying to use my linked list length attribute. It was returning 1 even though 
   everything was poped out and there where no values in the linked list. So I implemented the length, adding, and subtracting here in the Stack class.
"""

# Implemented with ARRAY
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.storage.append(value)

#     def pop(self):
#         if len(self.storage) == 0:
#             return None
#         else:
#             return self.storage.pop()


# Implemented with LINKED LIST
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.size = self.size + 1
        self.storage.add_to_tail(value)

    def pop(self):
        if self.size == 0:
            self.size = 0
        else:
            self.size = self.size - 1
        return self.storage.remove_tail()


