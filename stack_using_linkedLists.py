class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.head=None
    def isempty(self):
        if self.head==None:
            return True
        else:
            return False
    def push(self,data):
        new_node=node(data)
        if self.head==None:
            self.head=new_node
            return
        new_node.next=self.head
        self.head=new_node
    def pop(self):
        if self.isempty():
            print("stack is already empty")
        else:
            top=self.head
            self.head=self.head.next
            top.next=None
            return top
    def peek(self):
        top=self.head
        return top.data
    def display(self):
        iter=self.head
        while(iter!=None):
            print(iter.data,end=" ")
            iter=iter.next
if __name__=="__main__":
    s=stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.display()
    print("\ntop element from the stack =",s.peek())
    s.pop()
    s.display()
