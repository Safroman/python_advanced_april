class Stack:

    def __init__(self):
        self._stack = list()
        self._len = len(self._stack)

    def __str__(self):
        return f'{self._stack}'

    def len(self):
        return len(self._stack)

    def push(self, new_el):
        self._stack.append(new_el)
        self._len = len(self._stack)

    def pop(self):

        if self._len == 0:
            print('Stack is empty')
        else:
            next_out = self._stack.pop()
            self._len = len(self._stack)
            return next_out

    def peek(self):
        return self._stack[-1]


s = Stack()
my_list = [1, 2, 3, 4, 5]

for el in my_list:
    s.push(el)

print(s)

s.peek()

next_out = s.pop()
print(next_out)

s.push(7)
print(s)

for i in range(s.len()+1):
    print(s.pop())
