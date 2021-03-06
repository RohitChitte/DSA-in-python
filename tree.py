# tree is recursive data structure i.e node will have child node which itself is a tree
# children will have differnt nodes which are other instance of same treenode class. 
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = [] 
        self.parent = None

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            p = p.parent 
            level += 1
        return level

    def print_tree(self):
        #print(3*(self.get_level())*" ",self.data)
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if len(self.children)>0:
            for child in self.children:
                child.print_tree()


def build_product_tree():

    root = TreeNode("Electronics")
    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    root.print_tree()
    #print(laptop.children[0].get_level())  #getting level of 0th child of laptop 
 
#root  = build_product_tree()
#print(root.children[0].data)  #  printing the root nodes children lists 0 th items data
build_product_tree()