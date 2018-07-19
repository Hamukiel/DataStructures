class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def push(self, data):
        new = Node(data=data)
        new.next = self.root
        self.root = new

    def pop(self):
        if self.is_empty():
            return None
        ret = self.root
        self.root = ret.next
        return ret.data

    def peek(self):
        if self.is_empty():
            return None
        return self.root.data

    def infix_to_postfix(self, expression):
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        open_containers = {'(': ')', '[': ']', '{': '}'}
        close_containers = {')': '(', ']': '[', '}': '{'}
        res = ''

        for i in expression:
            if i in open_containers:
                self.push(i)
            elif i in close_containers:
                while (not self.is_empty()) and (self.peek() != close_containers[i]):
                    res = res + self.pop()
                if self.is_empty():
                    return None
                else:
                    self.pop()
            elif i in precedence:
                while (not self.is_empty()) and\
                        (self.peek() in precedence and precedence[self.peek()] >= precedence[i]):
                    res = res + self.pop()
                self.push(i)
            else:
                res = res + i

        while not self.is_empty():
            res = res + self.pop()

        return res


class StackedQueue:

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, data):
        self.stack1.push(data)

    def dequeue(self):
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

    def is_empty(self):
        return self.stack1.is_empty() and self.stack2.is_empty()


class DLLStack:

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        self.count = 0
        self.head = None
        self.middle = None

    def push(self, data):
        new = self.Node(data)
        self.count += 1
        if self.head is None:
            self.middle = self.head = new
        else:
            new.next = self.head
            new.next.prev = new
            if self.count % 2 > 0:
                self.middle = self.middle.prev

    def pop(self):
        if self.head is None:
            return None
        ret = self.head
        self.count -= 1
        self.head = ret.next
        if self.head is not None:
            self.head.prev = None
        if self.count % 2 == 0:
            self.middle = self.middle.next
        return ret.data

    def find_middle(self):
        if self.middle is None:
            return None
        return self.middle.data

    def delete_middle(self):
        if self.middle is None:
            return None
        self.middle.next.prev = self.middle.prev
        self.middle.prev.next = self.middle.next
        self.count -= 1
        if self.count % 2 == 0:
            self.middle = self.middle.next
        else:
            self.middle = self.middle.prev
