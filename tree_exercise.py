
# Tree Exercise 1 printing names and designaitons. 

class TreeNode:
    def __init__(self,data,designation):
        self.data = data
        self.designation = designation
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

    def print_tree(self,type):
        """
        #print(3*(self.get_level())*" ",self.data)
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if len(self.children)>0:
            for child in self.children:
                child.print_tree()
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
        

def build_product_tree(type):
    Nilupul = TreeNode("Nilupul","CEO")
    Chinmay = TreeNode("Chinmay","CTO")
    Vishwa = TreeNode("Vishwa","Infarstructure Head")
    Vishwa.add_child(TreeNode("Dhaval","Cloud Manager"))
    Vishwa.add_child(TreeNode("Abijit","App Manager"))
    Aamir = TreeNode("Amir","Application Head")
    Chinmay.add_child(Vishwa)
    Chinmay.add_child(Aamir)
    Gel = TreeNode("Gel","HR Head")
    Gel.add_child(TreeNode("Peter","Recruitment Manager"))
    Gel.add_child(TreeNode("Waqas","Policy Manager"))
    Nilupul.add_child(Chinmay)
    Nilupul.add_child(Gel)

    Nilupul.print_tree(type)

build_product_tree("nameaa")