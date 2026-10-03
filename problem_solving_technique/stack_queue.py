class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        if not self.items:
            return None
        return self.items.pop()

    def peek(self):
        return self.items[-1] if self.items else None


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, val):
        self.items.append(val)

    def dequeue(self):
        if not self.items:
            return None
        return self.items.pop(0)


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    print(s.pop())

    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    print(q.dequeue())
