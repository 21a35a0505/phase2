'''
class Queue:
    arr=[]
    size=5
    def enqueue(self,element):
        if len(self.arr)>=5:
            print('Queue is full')
        else:
            self.arr.append(element)
    def dequeue(self):
        if len(self.arr)==0:
            print('Queue is empty')
        else:
            q.arr=q.arr[::-1]
            self.arr.pop(0)
            q.arr=q.arr[::-1]
    def peek(self):
        if len(self.arr)==0:
            print('Queue is empty')
        else:
            return self.arr[-1]
    def isEmpty(self):
        if len(self.arr)==0:
            return True
        else:
            return False

q=Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
print(q.arr)
q.dequeue()
q.dequeue()
print(q.arr)
'''
#reverse 2nd half of queue
class Queue:
    arr=[]
    temp=[]
    size=10
    def enqueue(self,element):
        if len(self.arr)>=self.size:
            print('Queue is full')
        else:
            self.arr.append(element)
    def dequeue(self):
        if len(self.arr)==0:
            print('Queue is empty')
        else:
            self.arr.pop(0)
    def peek(self):
        if len(self.arr)==0:
            print('Queue is empty')
        else:
            return self.arr[-1]
    def isEmpty(self):
        if len(self.arr)==0:
            return True
        else:
            return False
    def print_queue(self):
        mid=len(self.arr)//2
        for i in range(mid):
            self.temp.append(self.arr.pop())
        for i in range(mid):
            self.arr.append(self.temp.pop(0))
        print(self.arr)

q=Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.enqueue(60)
q.enqueue(70)
q.enqueue(80)
print(q.arr)
q.dequeue()
q.dequeue()
q.print_queue()
