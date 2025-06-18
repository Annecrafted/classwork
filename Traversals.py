class TreeNode:

    def __init__(self,value):

        self.left=None

        self.right=None
        self.value=value

    def insert(self,key):

       if key < self.value:

           if self.left is None:
               self.left= TreeNode(key)
           else:
               self.left.insert(key)

       elif  key > self.value:

          if self.right is None:
              self.right = TreeNode(key)
          else:
              self.right.insert(key)

    def find(self,key):
        if key < self.value:
            if self.left is None:
                return False
            else:
                return self.left.find(key)
        elif key >self.value:
            if self.right is None:
                return False
            else:
                return self.right.find(key)
        else:
            return True

    def preorder_traversal(self):


        print(self.value)

        if self.left:
            self.left.preorder_traversal()

        if self.right:
            self.right.preorder_traversal()

    def inorder_traversal(self):

        if self.left:
            self.left.inorder_traversal()

        print(self.value)

        if self.right:
            self.right.inorder_traversal()

    def postorder_traversal(self):

        if self.left:
            self.left.postorder_traversal()


        if self.right:
            self.right.postorder_traversal()

        print(self.value)

if __name__ == '__main__':
    tree = TreeNode(10)

    tree.insert(5)
    tree.insert(3)
    tree.insert(4)
    tree.insert(11)
    tree.insert(12)
    tree.insert(13)

    tree.preorder_traversal()

 # tree.inorder_traversal()

# tree.postorder_traversal()

