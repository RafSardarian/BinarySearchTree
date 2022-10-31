class BST:
"""Binary Search Tree Data Structure

Example how to use:
    a = BST() ("a" is a new tree) 

Functions:
    a.insert(arg): takes only one positional argument
    1.first insertion will be a root
    2.you can't insert more than one value at once
    3.you can't insert multiple type values in one tree
##################################################
    a.preorder(): doesn't takes any argument
##################################################    
    a.inorder(): doesn't takes any argument
##################################################
    a.postorder(): doesn't takes any argument
##################################################
    a.levelorder([a.get_root()]): in argument takes get_root() function 
##################################################    
    a.find(arg): takes only one positional argument
##################################################
    a.clear(): doesn't takes any argument
##################################################    
    a.erase(arg): takes only one positional argument
##################################################    
    a.height(): doesn't takes any argument
##################################################    
    a.get_number_of_nodes(): doesn't takes any argument
##################################################
    a.__add__(b):
    1.where "b" is another tree announced in advance.
    2.you can use __add__ only with integers,lists and tuples.

"""
    def __init__(self,value=None):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)

    def insert(self,node):
        if not isinstance(node,BST):
            node = BST(node)
        if self.value is None:
            self.value = node
        else:
            self._insert(self.value,node)

    def _insert(self,current,node):
        if node.value < current.value:
            if current.left is None:
                current.left = node
            else:
                self._insert(current.left,node)
        else:
            if current.right is None:
                current.right = node
            else:
                self._insert(current.right,node)

##############PREORDER##############
    def pre_order(self):
        """root -> left -> right. Doesn't takes any argument"""
        self._pre_order(self.value)

    def _pre_order(self,current):
        if current:
            print(current.value)
            self._pre_order(current.left)
            self._pre_order(current.right)

##############INORDER##############
    def in_order(self):
        """left -> root -> right.Doesn't takes any argument"""
        self._in_order(self.value)

    def _in_order(self,current):
        if current:
            self._in_order(current.left)
            print(current.value)
            self._in_order(current.right)

##############POSTORDER##############
    def post_order(self):
        """left -> right -> root.Doesn't takes any argument"""
        self._post_order(self.value)

    def _post_order(self,current):
        if current:
            self._post_order(current.left)
            self._post_order(current.right)
            print(current.value)

##############LEVELORDER##############
    def get_root(self):
        return self.value

    def level_order(self,tree):
        """process all nodes of a tree by traversing through depth, first the root, then the child of the root, etc."""
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
            print(' <> '.join([str(x) for x in data]))
        self.level_order(new_tree)

##############FIND##############
    def find(self,target):
        """will check either the value is exist or not"""
        return self._find(self.value,target)

    def _find(self,current,target):
        if current:
            if current.value == target:
                return True
            elif target < current.value:
                return self._find(current.left,target)
            else:
                return self._find(current.right,target)
        return "NOT FOUND"

##############ERASE##############

    def erase(self,target):
        """takes one positional argument and deletes it"""
        self._erase(self.value,target,None,None)

    def _erase(self,current,target,parent,is_left):
        if current:#1
            if current.value == target:#2
                if current.left is None and current.right is None:#3
                    if parent:#4
                        if is_left:
                            parent.left = None
                        else:
                            parent.right = None
                    else:#4
                        self.value = None
                elif current.left is None:#3
                    if parent:#4
                        if is_left:
                            parent.left = current.right
                        else:
                            parent.right = current.right

                    else:#4
                        self.value = current.right
                elif current.right is None:#3
                    if parent:#4
                        if is_left:
                            parent.left = current.left
                        else:
                            parent.right = current.left
                    else:#4
                        self.value = current.left
                else:#3
                    min_right = self.get_min_right(current.right)
                    current.value = min_right.value
                    self._erase(current.right,min_right.value,current,False)

            elif target < current.value:#2
                return self._erase(current.left,target,current,True)

            else:#2
                return self._erase(current.right,target,current,False)

    def get_min_right(self,current):
        if current.left is None:
            return current
        else:
            return self.get_min_right(current.left)

##############CLEAR##############
    def clear(self):
        """deletes all data in tree"""
        self.left = None
        self.right = None
        self.value = None

##############GET NUMBER OF NODES##############
    def get_number_of_nodes(self,node):
        """node's count """
        if node is None:
            return 0
        return 1 + self.get_number_of_nodes(node.left) + self.get_number_of_nodes(node.right)

##############HEIGHT##############
    def height(self):
        if self.value != None:
            return self._height(self.value,0)
        else:
            return 0
    def _height(self,current_node,current_height):
        if current_node is None: return current_height
        left_height = self._height(current_node.left,current_height + 1)
        right_height = self._height(current_node.right,current_height + 1)
        return max(left_height,right_height)

##############OPERATOR ADD##############
    def __add__(self, arg):

        if not self and not arg:
            return None

        first_value = self.value if self else 0
        second_value = arg.value if arg else 0

        res = BST(first_value + second_value)

        res.left = BST.__add__(self.left if self else None, arg.left if arg else None)
        res.right = BST.__add__(self.right if self else None, arg.right if arg else None)
        return res


