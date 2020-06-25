"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):

        # compare the value thats being passed in to the current node
        if value < self.value:
            # check if left child node is equal to none
            if self.left is None:
                # if there is no where else to go 
                # create a new node with the input value and set it equal to the left child node
                self.left = BSTNode(value)
            else:
                # we re run this insert function with new left child value to compare against
               self.left.insert(value)
        # if the value being passed in is greater than the current node then
        # check right child node to see if its none. If it is, create a new node
        # and set it to the right child node. if not just re run current function
        # with new value to compate against  
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value) 
        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if the current node value is equal to the target value the return true
        if self.value == target:
            return True

        # If the target value is less than than current node value 
        # check if the left side is none. If so return 
        # false because we have reached end of the path.
        # If the left side is not not none then re run
        # the contains function on the new value.
        if target < self.value:
            if self.left is None:
                return False
            return self.left.contains(target)
        # same as above just this time we check if current value is greater than the target and
        # if so we go to the right instead
        if target > self.value:
            if self.right is None:
                return False
            return self.right.contains(target)

        

    # Return the maximum value found in the tree
    def get_max(self):
        # first make sure BST is not empty 
        if self.value is None:
            return None

        # search the BST until we get to the bottom value on the right side
        # then return that value
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        # check each side, if its there call it's for_each method
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
       
        # go all the way to the left then print that node
        if self.left:
            self.left.in_order_print(node)
        print(self.value)
        # then go right and print that node
        if self.right:
            self.right.in_order_print(node)
      

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # create a queue for nodes 
        queue = []
        # add first node to the queue
        queue.append(self)
        # while queue is not empty 
        while len(queue) > 0:
            # remove the first node
            current_node = queue.pop(0)
             # print the removed node
            print(current_node.value)
             # add all children into the queue
            if current_node.right:
                queue.append(current_node.right)
            if current_node.left:
                queue.append(current_node.left)
            

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # create stack for nodes that is visited
        stack = []
        # add first node to stack which will be the root node
        stack.append(self)
        # while stack is not empty 
        while len(stack) > 0:
            # pop off the stack
            current_node = stack.pop()
            # print that nodes value
            print(current_node.value)
            # add its children to stack 
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)
           
            
    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
