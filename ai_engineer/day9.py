class box:
    def __init__(self,data):
        self.data = data
        self.next = None
class link:
    def __init__(self):
        self.head = None
    def insert(self, data):
        new=box(data)
        if self.head is None:
            self.head=new
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,"->", end=' ')
            temp=temp.next
        print("None")
l=link()
l.insert(10)
l.insert(20)
l.insert(30)
l.insert(40)
l.display()
class stacki:
    def __init__(self):
        self.queue=[]
    def push(self,item):
        self.queue.append(item)
    def pop(self):
        if not self.is_empty():
            return self.queue.pop(0)
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
    def is_empty(self):
        return len(self.queue) == 0
    def display(self):
        print("Stack:", self.queue)
s=stacki()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.display()
s.pop()
s.display()
class x:
    def __init__(self):
        self.queue=[]
    def add(self,item):
        return self.queue.append(item)
    def delu(self):
        if not self.is_emp():
            return self.queue.pop(0)
    def peek(self):
        if not self.is_emp():
            return self.queue[0]
    def is_emp(self):
        return len(self.queue)==0
    def printu(self):
        print(self.queue)
q = x()
q.add(10)
q.add(20)
q.add(30)
q.printu()         # [10, 20, 30]
print(q.peek())    # 10
q.delu()           
q.printu()       
