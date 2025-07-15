class CircularQueue:

    DEFAULT_CAPACITY = 10

    def __init__(self):

        self._data= [None] * CircularQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):

        return self._size

    def is_empty(self):

        return self._size == 0 #return true if ._size == 0  return false otherwise

    def first(self):

        if self .is_empty():
            raise Empty("Queue is empty") #nothing else will be executed from here
        return self._data[self._front]

    def enqueue(self,data):

        if self._size == len(self._data):
            self._resize(2 * len(self._data))

        tail=(self._front + self._size) % len(self._data)
        self._data[tail]=data
        self._size += 1

    def dequeue(self):

        if self.is_empty():
            raise Empty("Queue is empty for Dequeue operation")

        front = (self._front + 1) % len(self._data)

        dequeued_data = self._data[self._front]
        self._data[self._front] = None  # Garbage collection

        self._size -= 1
        return dequeued_data

    def resize(self, new_capacity):
            ...

class Empty(Exception):
    pass

if __name__ == '__main__':
    obj1 = CircularQueue()

    insert_data = [11, 22, 33, 44, 55]

    for data in insert_data:
        obj1.enqueue(data)

        print(f"Add Element: {data}")
        print(f"the new size of the queue: {len(obj1)}")


