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
    def Inorder(self,root):
        temp=root
        if temp.left!=None:
            self.Inorder(temp.left)
        print(temp.data)
        if temp.right!=None:
            self.Inorder(temp.right)
    def preorder(self,root):
        temp=root
        print(temp.data)
        if temp.left!=None:
            self.Inorder(temp.left)
        if temp.right!=None:
            self.Inorder(temp.right)
    def postorder(self,root):
        temp=root
        if temp.left!=None:
            self.Inorder(temp.left)
        if temp.right!=None:
            self.Inorder(temp.right)
        print(temp.data)
    def levelorder(self,root):
        q=[]
        q.append(root.data)
        while len(q)!=0:
            ele=q.pop(0)
            if root.left:
                q.append(root.left)
            if root.right:
                q.append(root.right)
            
            print(ele.data)
        if root.left:
            
        
root=Node(10)
bs=BStree()
bs.add_ele(root,20)
bs.add_ele(root,50)
bs.add_ele(root,5)
bs.add_ele(root,7)
bs.Inorder(root)
bs.preorder(root)
bs.postorder(root)

                
                
