class Queue:

    def __init__(self):
        self._queue = list()
        self._len = len(self._queue)

    def __str__(self):
        return f'{self._queue}'

    def len(self):
        return len(self._queue)

    def enqueue(self, new_el):
        self._queue.append(new_el)
        self._len = len(self._queue)

    def dequeue(self):

        if self._len == 0:
            print('Queue is empty')
        else:
            next_out = self._queue.pop(0)
            self._len = len(self._queue)
            return next_out

q = Queue()
my_list = [1, 2, 3, 4, 5]

for el in my_list:
    q.enqueue(el)

print(q)

next_out = q.dequeue()
print(next_out)

q.enqueue(6)
print(q)

for i in range(q.len()+1):
    print(q.dequeue())

