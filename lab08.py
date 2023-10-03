class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,item1):
        self.stack.append(item1)
    def pop(self,item1):
              print("popped",self.stack.pop())
    def view(self):
            print(self.stack)
    def size(self):
        print("the size of the stack is ",len(self.stack))   
    def top(self):
         print(self.stack[-1])    
    def empty(self):
        if len(self.stack)==0:
             print("empty stack")
        else:
             print("stack is not empty")
stack1 = Stack()
stack1.push(10)
stack1.push(12)
stack1.push(13)
stack1.pop(12)
stack1.view()
stack1.size()
stack1.empty()
stack1.top()