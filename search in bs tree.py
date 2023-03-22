class Node:
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None
class BStree:
    def add_ele(self,root,value):
        new_node=Node(value)
        if new_node.data<root.data:
            if root.left==None:
                root.left=new_node
            else:
                self.add_ele(root.left,value)
        else:
            if root.right==None:
                root.right=new_node
            else:
                self.add_ele(root.right,value)
    def search(self,value,root):
        temp=root
        if temp.left!=None:
            self.search(value,temp.left)
        if temp.right!=None:
            self.search(value,temp.right)
        if temp.data==value:
            return root
    def height(self,root):
        if root==None:
            return -1
        left_height=self.height(root.left)
        right_height=self.height(root.right)
        return 1+max(left_height,right_height)
        
            
root=Node(10)
bs=BStree()
bs.add_ele(root,20)
bs.add_ele(root,50)
bs.add_ele(root,5)
bs.add_ele(root,7)
bs.add_ele(root,70)
print(bs.height(root))
        
