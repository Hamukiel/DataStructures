class Node:

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def insert(self, data):
        if data < self.data:
            if self.left_child is None:
                self. left_child = Node(data)
            else:
                self.left_child.insert(data)
        else:
            if self.right_child is None:
                self.right_child = Node(data)
            else:
                self.right_child.insert(data)

    def search(self, data):
        if self.data == data:
            return self
        if data < self.data:
            if self.left_child is None:
                return None
            else:
                return self.left_child.search(data)
        else:
            if self.right_child is None:
                return None
            else:
                return self.right_child.search(data)

    def min(self):
        if self.left_child is None:
            return self
        else:
            return self.left_child.min()

    def max(self):
        if self.right_child is None:
            return self
        else:
            return self.right_child.max()

    def delete(self, data):
        if data < self.data:
            if self.left_child is None:
                return self
            else:
                self.left_child = self.left_child.delete(data)
                return self
        elif data > self.data:
            if self.right_child is None:
                return self
            else:
                self.right_child = self.right_child.delete(data)
                return self
        else:
            if self.left_child is None:
                return self.right_child
            elif self.right_child is None:
                return self.left_child
            else:
                temp = self.left_child.max()
                self.data = temp.data
                self.left_child = self.left_child.delete(temp.data)
                return self