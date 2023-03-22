
class Node:
    def __init__(self,value):
        flo_name,flowers=value.split()
        self.flower=flo_name
        self.flowers=int(flowers)
        self.next=None
        self.temp=None
class Flower:
    def add_flo(self,head,value):
        flo_name,flowers=value.split()
        temp=head
        while temp!=None:
            if temp.flower==flo_name:
                temp.flowers=temp.flowers+int(flowers)
                break
            else:
                temp=temp.next
        if temp==None:
            new_flo=Node(value)
            head.next=new_flo
    def print_list(self,head):
        temp=head
        while temp!=None:
            print(temp.flower,temp.flowers)
            temp=temp.next
head=Node(input())
fl=Flower()
fl.add_flo(head,input())
fl.print_list(head)
