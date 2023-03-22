class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
class LinkedList:
    def add_ele(self,head,value):
        if head==None:
            head=Node(value)
        else:
            new_node=Node(value)
            temp=head
            while temp.next!=None:
                temp=temp.next
            temp.next=new_node
    def remove_ele(self,head):
        if head == None:
            print('List is empty')
        else:
            temp=head
            while temp.next.next!=None:
                temp=temp.next
            temp.next=None
    def reverse(head):
        cur=head
        prev=None
        while cur!=None:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
        return prev
    def print_List(self,head):
        temp=head
        while temp!=None:
            print(temp.data)
            temp=temp.next
    def search_ele(self):
        pass
    def add_at_begin(self,head,value):
        newnode=Node(value)
        newnode.next=head
        head=newnode
    def add_at_pos(self,head,value,pos):
        new_node=Node(value)
        curr=head
        prev=None
        while pos!=0:
            prev=curr
            curr=curr.next
            pos-=1
        prev.next=new_node
        new_node.next=curr

obj=LinkedList()
head=Node(10)
obj.add_ele(head,20)
obj.add_ele(head,30)
obj.add_ele(head,40)
obj.remove_ele(head)

#obj.add_at_begin(head,50)
#obj.add_at_pos(head,50,2)
obj.print_List(head)
