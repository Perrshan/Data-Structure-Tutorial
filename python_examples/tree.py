class Node:

    def __init__(self, data):
        
        self.data = data
        self.left = None
        self.right = None

class Binary_Search_Tree:

    def __init__(self):
        
        self.root = None

    # to insert we use the callable function and if the tree is not empty then we will call the inner _insert function
    def insert(self, data):

        # if tree is empty
        if self.root is None:
            self.root = Node(data)

        else:
            self._insert(data, self.root)

    # inner function to process the insert of a nonempty tree
    def _insert(self, data, node):

        
        # have to alter the _insert function
        # -------------------- SOLUTION ---------------------
        if data == node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(data, node.left)
        # -------------------- SOLUTION END -----------------

        # checks to see whether the data should go to the left or right branch of the current node
        elif data < node.data:
            # if left branch empty assign a new node to the left branch
            if node.left is None:
                node.left = Node(data)
            else:
                # recursion
                self._insert(data, node.left)
        else:
            # if right branch empty assign a new node to the right branch
            if node.right is None:
                node.right = Node(data)
            else:
                # recursion
                self._insert(data, node.right)

    # special method
    def __contains__(self, data):

        return self._contains(data, self.root)
    

    def _contains(self, data, node):

        # value not in list
        if node == None:
            return False
        
        # found value
        if data == node.data:
            return True
        
        # checks to see if the data is in the left or right branch
        elif data < node.data:
            return self._contains(data, node.left)
        else:
            return self._contains(data, node.right)
        

    # special method
    def __iter__(self):

        yield from self._traverse_forward(self.root)

    def _traverse_forward(self, node):

        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)

    # special method
    def __reversed__(self):

        yield from self._traverse_backward(self.root)

    def _traverse_backward(self, node):

        if node is not None:
            yield from self._traverse_backward(node.right)
            yield node.data
            yield from self._traverse_backward(node.left)


    def get_height(self):

        # tree is empty
        if self.root is None:
            return 0
        else:
            return self._get_height(self.root)
        

    def _get_height(self, node):

        # current node is empty
        if node is None:
            return 0
        else:

            # compare length of left and right branches recursively
            left_height = self._get_height(node.left)
            right_height = self._get_height(node.right)
            return max(left_height, right_height) + 1

# -------------------- SOLUTION ---------------------
# Lines 29-36 has my edited _insert function as well

def factors(num):

    tree = Binary_Search_Tree()
    _factors(num, tree)
    return tree

def _factors(num, tree):

    divisor = 2

    while num % divisor != 0 and divisor < num**(0.5):
        divisor += 1
    
    if divisor > num**(0.5):
        tree.insert(num)
        return tree
    
    dividend = num // divisor
    
    tree.insert(divisor)

    _factors(dividend, tree)

num = 7654321
factor_tree = factors(num)

print(f'Number is {num}')

print('Factors: ', end='')
for x in reversed(factor_tree):
    print(x, end=', ')
print()

product = 1

for x in factor_tree:
    product *= x

print(f'Product: {product}')
