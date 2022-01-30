class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class stack_Linked_list:
    def __init__(self):
        self.head = None

    def printL(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def push(self, data):
        node = Node(data, self.head)
        self.head = node

    def pop(self):
        if self.head == None:
            return "Underflow condition"
        else:
            x = self.head.data
            self.head = self.head.next
            return x

    def peek(self,position):
        if position >= 1 and position <=self.get_length():
            #if position == 1:
            #    return self.head.data
            #else:
            count = 1
            itr = self.head
            while itr :
                if count == position:
                    return itr.data
                    break
                itr = itr.next
                count +=1
        else:
            return  "Invalid index"


    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)


    def search(self, key):
        itr = self.head
        while itr:
            if (itr.data == key):
                return itr
            itr = itr.next

    def stacktop(self):
        return self.head.data

    def isempty(self):
        if self.head == None:
            return True
        else:
            return False


def paranthesis_matching(string):
    ll = stack_Linked_list()
    for i in string :
        if i == '(':
            ll.push(i)
        elif i == ')':
            x = ll.pop()
    if ll.isempty() and x != "Underflow condition":
        return "Paranthesis Match"
    else:
        return "Paranthisis Don't Match"

def paranthesis_match_extension(string):
    ll = stack_Linked_list()
    for i in string:
        if i == "{" or i == "[" or i == '(':
            ll.push(i)
        elif i == "}" or i== "]" or i == ")":
            if ll.stacktop() == i:
                ll.pop()
            else:
                return "Unmatched"
    if ll.isempty() and x != "Underflow condition":
        return "Paranthesis Match"
    else:
        return "Paranthisis Don't Match"

# Function to check parentheses
def check(myStr):
    open_list = ["[", "{", "("]
    close_list = ["]", "}", ")"]

    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                    (open_list[pos] == stack[len(stack) - 1])):
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"

def paranthesis_match_extensin(string):
    """This Function evaluates paranthesis using stack linked lists """
    open_list = ["[", "{", "("]
    close_list = ["]", "}", ")"]
    l4 = stack_Linked_list()
    for i in string :
        if i in open_list:
            l4.push(i)
        elif i in close_list:
            pos = close_list.index(i)
            if l4.stacktop() == open_list[pos]:
                l4.pop()
            else:
                return "Unbalanced"
    if l4.isempty() :
        return "Balanced"
    else:
        return "Unbalanced"


def isOperand(char):
    if char == "+" or char == "-" or char == "/" or char == "*":
        return False
    else:
        return True

def precedence(char):
    if char == "+" or char == "-":
        return 1
    elif char == "*" or char == "/":
        return 2
    else:
        return 0

def infix_to_postfix(infix):
    """This Function converts infix expression to postfix expression"""
    postfix = list()
    l5 = stack_Linked_list()
    l5.push("#")   # pushing '#' into the stack to avoid error at  line if precedence(infix[i])>precedence(l5.stacktop()):
                        #
    i = 0
    while i<len(infix):
        if isOperand(infix[i]):
            postfix.append(str(infix[i]))
            i+=1
        else:

            if precedence(infix[i])>precedence(l5.stacktop()):
                l5.push(infix[i])
                i += 1
            else:
                postfix.append(str(l5.pop()))
    while (not l5.isempty()):
        postfix.append(l5.pop())
    return "".join(postfix)[0:len(postfix)-2]

def postfix_evaluation(postfix):
    l6 = stack_Linked_list()
    for i in postfix:
        if isOperand(i):
            l6.push(int(i))
        else:
            b = l6.pop()
            a = l6.pop()
            if i == "+":
                l6.push(int(a+b))
            elif i == "-":
                l6.push(int(a-b))
            elif i == "*":
                l6.push(int(a*b))
            elif i == "/":
                l6.push(int(a/b))
    return l6.pop()



if __name__ == '__main__':
    """
    l1 = stack_Linked_list()
    l1.push(21)
    l1.push(22)
    l1.push(0)
    l1.printL()
    print("Pop operation",l1.pop())
    l1.printL()
    print("peek 1st postion",l1.peek(1))
    print("peek 2md postion", l1.peek(2))
    print("peek 88th postion", l1.peek(88))
    print("Stacktop",l1.stacktop())
    print("Size of stack",l1.get_length())
    print("Empty status ",l1.isempty())
    
    """








    # Driver code
    string = "{[]{()}}"
    print(string, "-", check(string),paranthesis_match_extensin(string))

    string = "[{}{})(]"
    print(string, "-", check(string),paranthesis_match_extensin(string))

    string = "((()"
    print(string, "-", check(string),paranthesis_match_extensin(string))




    a = "((a+b)*(b-c))"
    b = "(((a+b)*(b-c))"
    c = "((a+b)*(b-c)))"
    d = "((()"
    e = "(((((())))))"
    """
    print(paranthesis_matching(a))
    print(paranthesis_matching(b))
    print(paranthesis_matching(c))
    print(paranthesis_matching(d))
    print(paranthesis_matching(e))
    """


    """
    ll = stack_Linked_list()
    ll.push(10)
    ll.push(20)
    ll.push(21)
    ll.push(23)
    ll.printL()
    print((ll.pop()))
    print(ll.stacktop()==21)
    """

    infix_1 = "a+b*c-d/e"
    print(infix_to_postfix(infix_1))
    postfix = "35*62/+4-"
    print(f"Evaluation of postfix expression {postfix} is : ",postfix_evaluation(postfix))

