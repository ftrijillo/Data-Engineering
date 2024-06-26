class Queue:
    def __init__(self):
        # Initialize an empty queue
        self.queue = []

    def enqueue(self, item):
        # Add the item to the back of the queue
        self.queue.append(item)

    def dequeue(self):
        # Remove and return the item from the front of the queue
        if len(self.queue) > 0:
            item = self.queue[0]
            self.queue = self.queue[1:]
            return item
        return None

    def peek(self):
        # Return the item at the front of the queue without removing it
        return self.queue[0] if len(self.queue) > 0 else None

    def is_empty(self):
        # Return True if the queue is empty, False otherwise
        return len(self.queue) == 0

    def size(self):
        # Return the number of items in the queue
        return len(self.queue)


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())  # Should print 1
print(queue.peek())  # Should print 2
print(queue.is_empty())  # Should print False
print(queue.size())  # Should print 2
