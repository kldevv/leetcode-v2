import threading

class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.enqueue_cnt = threading.Semaphore(capacity)
        self.dequeue_cnt = threading.Semaphore(0)
        self.lock = threading.Lock()
        self.storage = collections.deque()

    def enqueue(self, element: int) -> None:
        self.enqueue_cnt.acquire()
        with self.lock:
            self.storage.append(element)
        self.dequeue_cnt.release()

    def dequeue(self) -> int:
        self.dequeue_cnt.acquire()
        with self.lock:
            data = self.storage.popleft()
        self.enqueue_cnt.release()
        return data
    
    def size(self) -> int:
        return len(self.storage)

