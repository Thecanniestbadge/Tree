class node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None  # pointer to parent node in tree
    def peek(self):
        print ("left child", self.left_child)
        print ("Right Child", self.right_child)
        print ("parent", self.parent)

class binary_search_tree:
    def __init__(self):
        self.root = None  # Start with no root node

    def insert(self, value):
        if self.root is None:  # If no root, create the root node with the value
            self.root = node(value)
        else:
            self._insert(value, self.root)  # Find the insertion point
    
    def _insert(self, value, cur_node):
        if value < cur_node.value:  # New data to be a left child?
            if cur_node.left_child is None:  # Left child spot available?
                cur_node.left_child = node(value)  # Make it the left child
                cur_node.left_child.parent = cur_node  # Create a pointer back to the parent
            else:
                self._insert(value, cur_node.left_child)  # Left child full, look at left child
        elif value > cur_node.value:  # New data to be a right child?
            if cur_node.right_child is None:  # Right child spot available?
                cur_node.right_child = node(value)  # Make it the right child
                cur_node.right_child.parent = cur_node  # Create a pointer back to the parent
            else:
                self._insert(value, cur_node.right_child)  # Right child full, look at right child
        else:
            print("Value already in the Tree!")

    def print_tree(self):  # Print tree using inorder traversal
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node is not None:
            self._print_tree(cur_node.left_child)
            print(str(cur_node.value))
            self._print_tree(cur_node.right_child)

    def num_children(n):
        num_children=0
        if n.left_child!=None: num_children+=1
        if n.right_child!=None: num_children+=1
        return num_children
    
    def height(self):
        if self.root !=None:
           return self._height(self.root,0)
        else: 
            return 0
    def _height(self, cur_node, cur_height): #recursively check each node
        if cur_node == None: return cur_height
        left_height = self._height(cur_node.left_child, cur_height+1)
        right_height = self._height(cur_node.right_child, cur_height+1)
        return max(left_height, right_height)
    
    def search(self,value):
        if self.root!=None:
            return self._search(value,self.root)
        else:
            return False
        
    def _search(self,value,cur_node):
        if value==cur_node.value:
                return True
        elif value<cur_node.value and cur_node.left_child!=None:
                return self._search(value,cur_node.left_child)
        elif value>cur_node.value and cur_node.right_child!=None:
                return self._search(value,cur_node.right_child)
        return False
    
    def find(self,value):
        if self.root!=None:
            return self._find(value,self.root)
        else:
            return None

    def _find(self,value,cur_node):
        if value==cur_node.value:
            return cur_node
        elif value<cur_node.value and cur_node.left_child!=None:
            return self._find(value,cur_node.left_child)
        elif value>cur_node.value and cur_node.right_child!=None:
            return self._find(value,cur_node.right_child)

    def delete(self, value):
        if mytree.search(value):
            cur_node = mytree.find(value)
            self._delete(cur_node)
        else:
            print('Value '+ str(value)+ ' not in tree')

    def _delete(self, cur_node):
        print("Deleting node", cur_node.value)
        num_children = 0
        if cur_node.left_child != None:
            num_children += 1
        if cur_node.right_child != None:
            num_children += 1
        print("number of children", num_children)
        
        if num_children == 0:
            if cur_node.parent.left_child == cur_node:
                cur_node.parent.left_child = None
            if cur_node.parent.right_child == cur_node:
                cur_node.parent.right_child = None
        
        if num_children == 1:
            if (cur_node.parent.left_child == cur_node):
                if cur_node.left_child != None:
                    cur_node.parent.right_child = cur_node.left_child
                    cur_node.left_child.parent = cur_node.parent
                else:
                    cur_node.parent.left_child = cur_node.right_child
                    cur_node.right_child.parent = cur_node.parent
            if (cur_node.parent.right_child == cur_node):
                if cur_node.left_child != None:
                    cur_node.parent.right_child = cur_node.left_child
                    cur_node.left_child.parent = cur_node.parent
                else:
                    cur_node.parent.right_child = cur_node.right_child
                    cur_node.left_child.parent = cur_node.parent
        
        if num_children == 2: 
            successor = cur_node.right_child
        while successor.left_child != None:
            successor = successor.left_child
        cur_node.value = successor.value
        if successor.right_child != None:
            if successor.parent.left_child == successor:
                successor.parent.left_child = successor.right_child
            else:
                successor.parent.right_child = successor.right_child
            successor.right_child.parent = successor.parent
        else:
            if successor.parent.left_child == successor:
                successor.parent.left_child = None
            else:
                successor.parent.right_child = None
                

        
        

# helper code
mytree = binary_search_tree()
mytree.insert('b')
mytree.print_tree()
print("------------")
mytree.insert('f')
mytree.print_tree()
print("------------")
mytree.insert('a')
mytree.print_tree()
print("------------")
mytree.insert('d')
mytree.print_tree()
print("------------")
mytree.insert('x')
mytree.print_tree()
print("------------")
# print (mytree.height())

# print("Search for value d = ",mytree.search('d'))
# print("Search for value x = ",mytree.search('x'))

# print(mytree.find('b').right_child.value)

mytree.delete('f')
mytree.print_tree()
print("------------")
print(mytree.search('d'))
newnode = (mytree.find('b'))
newnode.peek()