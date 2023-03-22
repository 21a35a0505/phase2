class Queue:
    def __init__(self):
        temp=[]
        original=[]
    def enqueue(self,element):
        self.temp.append(element)
        while len(self.original)!=0:
            pop_ele=self.original.pop(0)
            self.temp.append(pop_ele)
        while len(self.original)!=0:
            pop_ele=self.temp.pop(0)
            self.original.append(pop_ele)
    def dequeue(self):
        return self.original.pop(0)
    def print_queue(self):
        print(self.original)

q=Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.print_queue()
