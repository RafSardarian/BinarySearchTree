class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)


class BST:


    def __init__(self):
        self.root = None


    def insert(self, node):
        if not isinstance(node, Node):
            node = Node(node)

        if self.root is None:
            self.root = node
            
        else:
            self._insert(self.root, node)


    def _insert(self, current, node):
        if node.value < current.value:
            if current.left is None:
                current.left = node
            else:
                self._insert(current.left,node)  
        else:
            if current.right is None:
                current.right = node 
            else:
                self._insert(current.right, node)
                


    def pre_order(self):
        self._pre_order(self.root)

    def _pre_order(self,current):
        if current:
            print(current.value)
            self._pre_order(current.left)
            self._pre_order(current.right)


   

    def in_order(self):
        self._in_order(self.root)


    def _in_order(self,current):
        if current:
            self._in_order(current.left)
            print(current.value)
            self._in_order(current.right)




    def post_order(self):
        self._post_order(self.root)

    def _post_order(self, current):
        if current:
            self._post_order(current.left)
            self._post_order(current.right)
            print(current.value)

    
    def get_root(self):
        return self.root


    def level_order(self, tree):
        new_tree = []
        data = []

        if not tree:
            return 
        else:
            for node in tree:
                data.append(node.value)
                if node.left is not None:
                    new_tree.append(node.left)
                if node.right is not None:
                    new_tree.append(node.right)
            print( ' <> '.join([str(x) for x in data]))
        
        self.level_order(new_tree)


  



    def find(self, target):
        return self._find(self.root, target)

    def _find(self, current, target):
        if current:
            if current.value == target:
                return True
            elif target < current.value:
                return self._find(current.left, target)
            else:
                return self._find(current.right, target)
        return "NOT FOUND"

   



    def erase(self, target):
        self._erase(self.root, target, None, None)


    def _erase(self, current, target, parent, is_left):
        if current:#1
            if current.value == target:#2
                if current.left is None and current.right is None:#3
                    if parent:#4
                        if is_left:
                            parent.left = None
                        else:
                            parent.right = None
                    
                    else:#4
                        self.root = None
                

                elif current.left is None:#3
                    if parent:#4
                        if is_left:
                            parent.left = current.right
                        else:
                            parent.right = current.right
                    
                    else:#4
                        parent.right = current.right


                elif current.right is None:#3
                    if parent:#4
                        if is_left:
                            parent.left = current.left
                        else:
                            parent.right = current.left
                    
                    else:#4
                        self.root = current.left


                else:#3
                    min_right = self.get_min_right(current.right)
                    current.value = min_right.value
                    self._erase(current.right, min_right.value, current, False)




            elif target < current.value:#2
                return self._erase(current.left, target, current, True)
            



            else:#2
                return self._erase(current.right, target, current, False)
    


    def clear(self):
        self.root = None
        #self.left = None
        #self.right = None
        return









   # def get_min_right(self, current):
       # if current.left is None:
           # return current
        #else:
            #return self.get_min_right(current.left)



    

    def get_number_of_nodes(self,node):
        if node is None:
            return 0
        return 1 + self.get_number_of_nodes(node.left) + self.get_number_of_nodes(node.right)

    def height(self):
        if self.root != None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, current_node, current_height):
        if current_node == None: return current_height
        left_height = self._height(current_node.left, current_height + 1)
        right_height = self._height(current_node.right, current_height + 1)
        return max(left_height, right_height)


    #def mergeTrees(tree1, tree2):
        #if not tree1 and not tree2:
            #return None

        #value1 = tree1.value if tree1 else 0
        #value2 = tree2.value if tree2 else 0
        #root = BST(value1 + value2)

        #root.left = self.mergeTrees(tree1.left if tree1 else None, tree2.left if tree2 else None)
        #root.right = self.mergeTrees(tree1.right if tree1 else None, tree2.right if tree2 else None)

        #return root
   



"""
a = BST()


b = BST()

root = BST()

a.insert(100)
a.insert(200)
a.insert(50)
a.insert(40)
a.insert(60)
a.insert(250)
a.insert(150)
a.insert(140)
a.insert(155)
a.insert(290)
a.insert(240)
a.insert(30)
a.insert(45)
a.insert(70)
a.insert(59)


b.insert(200)
b.insert(100)
b.insert(300)
b.insert(350)
b.insert(250)
b.insert(50)
b.insert(150)
b.insert(40)
b.insert(50)
b.insert(130)
b.insert(220)

#print("height of a")
#print(a.height())
#print("height of b")
#print(b.height())
#a.clear()
root.addTrees(a,b)
#a.get_right()
#print(a.get_number_of_nodes(a.get_root()))
#print(b.get_number_of_nodes(b.get_root()))
#print(a.find(140))
#print(a.find(3000))
#a.clear()
#a.level_order([a.get_root()])
#a.get_number_of_nodes()
#a.in_order()
#b.in_order()
#b.level_order([b.get_root()])
"""
