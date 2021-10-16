class TreeNode:
    def __init__(self,data):
        self.data = data
        #self.designation = designation
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

    def print_tree(self,level):
        if self.get_level()<=level:
            #print(3*(self.get_level())*" ",self.data)
            spaces = ' ' * self.get_level() * 3
            prefix = spaces + "|__" if self.parent else ""
            print(prefix + self.data)
            if len(self.children)>0:
                for child in self.children:
                    child.print_tree(level)
            
        """
        if type=="name":
            #print(3*(self.get_level())*" ",self.data)
            spaces = ' ' * self.get_level() * 3
            prefix = spaces + "|__" if self.parent else ""
            print(prefix + self.data)
            if len(self.children)>0:
                for child in self.children:
                    child.print_tree(type)
        elif type == "both":
            #print(3*(self.get_level())*" ",self.data)
            spaces = ' ' * self.get_level() * 3
            prefix = spaces + "|__" if self.parent else ""
            print(prefix + self.data + f"  ({self.designation}) ")
            if len(self.children)>0:
                for child in self.children:
                    child.print_tree(type)

        else :
            #print(3*(self.get_level())*" ",self.data)
            spaces = ' ' * self.get_level() * 3
            prefix = spaces + "|__" if self.parent else ""
            print(prefix + self.designation)
            if len(self.children)>0:
                for child in self.children:
                    child.print_tree(type)
        """

def build_product_tree():
    root = TreeNode("Global")

    india = TreeNode("India")

    gujarat = TreeNode("Gujarat")
    gujarat.add_child(TreeNode("Ahmedabad"))
    gujarat.add_child(TreeNode("Baroda"))

    karnataka = TreeNode("Karnataka")
    karnataka.add_child(TreeNode("Bangluru"))
    karnataka.add_child(TreeNode("Mysore"))

    india.add_child(gujarat)
    india.add_child(karnataka)

    usa = TreeNode("USA")

    nj = TreeNode("New Jersey")
    nj.add_child(TreeNode("Princeton"))
    nj.add_child(TreeNode("Trenton"))

    california = TreeNode("California")
    california.add_child(TreeNode("San Francisco"))
    california.add_child(TreeNode("Mountain View"))
    california.add_child(TreeNode("Palo Alto"))

    usa.add_child(nj)
    usa.add_child(california)

    root.add_child(india)
    root.add_child(usa)
    root.print_tree(4)

build_product_tree()