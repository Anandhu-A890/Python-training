from collections import deque
class Queue:
    def __init__(self):
        self.queue=deque()
        print("Queue(using deque) created!")

    def enqueue(self,item):
        self.queue.append(item)
        print(f"Enqueued:{item}|Queue:{list(self.queue)}(<-Front|Rear->))")

    def dequeue(self):
        if not self.queue:
            print("Queue is empty")
            return None
        item=self.queue.popleft()
        print(f"Dequeue:{item}|Queue:{list(self.queue)}")
        return item
q=Queue()
q.enqueue(5)
q.enqueue(6)
q.enqueue(1)
q.enqueue(3)
q.dequeue()