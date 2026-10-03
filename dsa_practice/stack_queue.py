"""Stack and queue implementations.

This file demonstrates:
- stack operations: push, pop, peek
- queue operations: enqueue, dequeue, front
- balanced parentheses checking using a stack

These are core data structures used in many DSA problems.
"""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not self.items:
            return None
        return self.items.pop()

    def peek(self):
        if not self.items:
            return None
        return self.items[-1]


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if not self.items:
            return None
        return self.items.pop(0)

    def front(self):
        if not self.items:
            return None
        return self.items[0]


def is_balanced_parentheses(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if not stack or stack.pop() != pairs[ch]:
                return False
    return len(stack) == 0


if __name__ == "__main__":
    st = Stack()
    st.push(1)
    st.push(2)
    print(st.pop())

    q = Queue()
    q.enqueue(5)
    q.enqueue(6)
    print(q.dequeue())

    print(is_balanced_parentheses("{[()]}"))
