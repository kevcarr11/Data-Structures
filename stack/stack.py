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
"""
from linked_list import LinkedList 

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size
        # return len(self.storage)

    def push(self, value): 
        self.storage.add_to_head(value)
        self.size += 1
        # self.storage.insert(0, value)

    def pop(self):
        if self.size > 1:
            self.storage.remove_head()
            self.size -= 1
            return self.storage.head.value

        # if self.storage.__len__() < 1:
        #     print('List is empty')
        #     return
        # else:
        #     self.storage.pop(0)


test = Stack()
test.push(100)
test.push(101)
test.push(105)
# test.push(2)
# test.push(21)
# test.push(20)
# test.push(24)
# print(test.pop())

node = test.storage.head
while node:
    if node is None:
        None
    print(node.value)
    node = node.next_node

