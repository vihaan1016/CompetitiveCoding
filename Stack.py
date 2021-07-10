from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self, value):
        self.container.append(value)
    
    def pop(self):
        self.container.pop()
    
    def is_empty(self):
        return len(self.container) == 0
    
    def peek(self):
        return self.container[-1]
    
    def size(self):
        return len(self.container)

def reverse_string(s):
    stack = Stack()

    for ch in s:
        stack.push(ch)

    rstr = ''
    while stack.size()!=0:
        rstr += str(stack.pop())

    return rstr


if __name__ == '__main__':
    print(reverse_string("We will conquere COVI-19"))
    print(reverse_string("I am the king"))
   
s = Stack()
s.push(5)
s.push(4)
s.push(6)
s.push(8)
print("Last element of original stack: ", s.peek())
print("Orginal Size of the stack: ", s.size())

s.pop()
print("Last element of stack after removing last element: ", s.peek())
print("Size after popping of the stack: ", s.size())