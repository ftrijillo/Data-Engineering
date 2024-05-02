class Stack:
    def __init__(self):
        # Initialize an empty stack
        self.stack = []

    def push(self, item):
        # Push the item onto the stack
        self.stack.append(item)

    def pop(self):
        # Remove and return the item at the top of the stack
        return self.stack.pop() if len(self.stack) > 0 else None

    def peek(self):
        # Return the item at the top of the stack without removing it
        return self.stack[-1] if len(self.stack) > 0 else None

    def is_empty(self):
        # Return True if the stack is empty, False otherwise
        return len(self.stack) == 0

    def size(self):
        # Return the number of items in the stack
        return len(self.stack)


stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)

print(stack.pop())
print(stack.peek())
print(stack.is_empty())
print(stack.size())
