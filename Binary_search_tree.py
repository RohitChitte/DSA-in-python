# Search complexity O(logn) base 2. 

class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None 
        self.right = None

    def add_child(self,data):
        if data == self.data:
            return 
        if data < self.data :
            if self.left:
                self.left.add_child(data)
            else :
                self.left = BinarySearchTreeNode(data)
        else :
            if self.right :
                self.right.add_child(data)
            else :
                self.right = BinarySearchTreeNode(data)
    
    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def pre_order_traversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.in_order_traversal()
        
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        if self.right:
            elements += self.right.in_order_traversal()
        elements.append(self.data)
        return elements

    def search(self,data):
        if self.data == data:
            return True 
        if data < self.data:
            # value might be in left subtree
            if self.left:
                return self.left.search(data)
            else:
                return False
        if data > self.data:
            # value might be in right subtree
            if self.right:
                return self.right.search(data)
            else :
                return False
                
    def find_min(self):
        if self.left:
            return self.left.find_min()
        else :
            return self.data
    def find_max(self):
        if self.right:
            return self.right.find_max()
        else :
            return self.data

    def calculate_sum(self):
        elements = 0
        if self.left:
            elements += self.left.calculate_sum()
        if self.right:
            elements += self.right.calculate_sum()
        
        elements += self.data
        return elements 
    
    def delete(self,data):
        if self.data > data:
            if self.left:
                self.left = self.left.delete(data)
        elif self.data < data:
            if self.right:
                self.right = self.right.delete(data)
        else:
            if self.left is None  and self.right is None:
                return None
            if self.left is None :
                return self.right
            if self.right is None:
                return self.left   

            min_val = self.right.find_min()
            self.data = min_val  
            self.right = self.right.delete(min_val)    

        return self
        

    # This is code basics approach. 
    """
    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum
    """

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

numbers = [17,4,1,20,9,23,18,34]
numbers_tree = build_tree(numbers)
numbers_tree.delete(20)
print(numbers_tree.in_order_traversal())
#print(numbers_tree.pre_order_traversal())
#print(numbers_tree.post_order_traversal()) 
#print(numbers_tree.calculate_sum())    
#print(numbers_tree.search(34))     
#print(numbers_tree.find_min())
#print(numbers_tree.find_max())

