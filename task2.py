from collections import deque
import time
# Queue implementation using lists
class ListQueue:
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        raise IndexError("dequeue from empty queue")
    def is_empty(self):
        return len(self.queue) == 0
# Queue implementation using collections.deque
class DequeQueue:
    def __init__(self):
        self.queue = deque()
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        raise IndexError("dequeue from empty queue")
    def is_empty(self):
        return len(self.queue) == 0
# Performance comparison
def performance_test():
    list_queue = ListQueue()
    deque_queue = DequeQueue()
    # Enqueue items from console
    while True:
        item = input("Enter an item to enqueue (or type 'exit' to stop): ")
        if item.lower() == 'exit':
            break
        list_queue.enqueue(item)
        deque_queue.enqueue(item)
    # Dequeue test
    print("Dequeuing items from both queues...")
    while not list_queue.is_empty():
        list_queue.dequeue()
    while not deque_queue.is_empty():
        deque_queue.dequeue()
if __name__ == "__main__":
    performance_test()
