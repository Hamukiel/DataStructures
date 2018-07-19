from queue import Queue
from src.doubly_linked_list import DoublyLinkedList, Node as DLLNode


class Node:

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def __str__(self):
        return self.str_in_order()

    @staticmethod
    def build_from_array(array):
        length = len(array)
        if length == 0:
            return None
        if length == 1:
            return Node(array[0])

        middle = length//2
        root = Node(array[middle])
        root.left_child = Node.build_from_array(array[0:middle])
        root.right_child = Node.build_from_array(array[middle+1:length])
        return root

    def balance(self):
        def to_array(node, array):
            if node.left_child is not None:
                to_array(node.left_child, array)
            array.append(node.data)
            if node.right_child is not None:
                to_array(node.right_child, array)

        array = []
        to_array(self, array)
        return Node.build_from_array(array)


    def get_sum_tree(self):
        if self.left_child is None and self.right_child is None:
            return Node(0), self.data
        left = right = None
        left_value = right_value = 0
        if self.left_child is not None:
            left, left_value = self.left_child.get_sum_tree()
        if self.right_child is not None:
            right, right_value = self.right_child.get_sum_tree()
        value = left_value + right_value
        root = Node(value)
        root.left_child = left
        root.right_child = right
        return root, value+self.data


    def get_level(self, data1, level):
        if self.data == data1:
            return level
        left = -1
        if self.left_child is not None:
            left = self.left_child.get_level(data1, level+1)
        if left == -1:
            if self.right_child is not None:
                left = self.right_child.get_level(data1, level + 1)
        return left

    def distance(self, data1, data2):
        lca = self.fast_lca(data1, data2)
        d1 = lca.get_level(data1, 0)
        d2 = lca.get_level(data2, 0)
        return d1 + d2

    def fast_lca(self, data1, data2):
        if self.data == data1 or self.data == data2:
            return self
        if self.left_child:
            left_lca = self.left_child.fast_lca(data1, data2)
        else:
            left_lca = None
        if self.right_child:
            right_lca = self.right_child.fast_lca(data1, data2)
        else:
            right_lca = None
        if left_lca and right_lca:
            return self
        return left_lca if left_lca is not None else right_lca

    def get_path(self, path, data):
        path.append(self)
        if self.data == data:
            return True
        if ((self.left_child is not None and self.left_child.get_path(path, data))
                or (self.right_child is not None and self.right_child.get_path(path, data))):
            return True
        path.pop()
        return False

    def lca(self, data1, data2):
        path_a = []
        path_b = []
        if (not self.get_path(path_a, data1)) or (not self.get_path(path_b, data2)):
            return -1
        i = 0
        while i < len(path_a) and i < len(path_b):
            if path_a[i] != path_b[i]:
                return path_a[i-1]
            i += 1

    def sorted_lca(self, data1, data2):
        if data2 < self.data and data1 < self.data:
            if self.left_child is not None:
                return self.left_child.sorted_lca(data1, data2)
            else:
                return None
        if data1 > self.data and data2 > self.data:
            if self.right_child is not None:
                return self.right_child.sorted_lca(data1, data2)
            else:
                return None

        return self

    @staticmethod
    def build_special_tree(pre_order, pre_nl):
        if pre_order is None or len(pre_order) < 1:
            return None

        root = Node(pre_order[0])
        length = len(pre_order)
        if pre_nl[0] == 'L':
            return root, 1
        root.left_child, lindex = Node.build_special_tree(pre_order[1:length], pre_nl[1: length])
        root.right_child, rindex = Node.build_special_tree(pre_order[lindex+1: length], pre_nl[lindex+1: length])
        return root, lindex + rindex + 1




    @staticmethod
    def build_tree_pre_post(pre_order, post_order):
        if pre_order is None or len(pre_order) < 1:
            return None

        root = Node(pre_order[0])
        length = len(pre_order)
        if length == 1:
            return root
        index = post_order.index(pre_order[1])
        root.left_child = Node.build_tree_pre_post(pre_order[1:index+2], post_order[0:index+1])
        root.right_child = Node.build_tree_pre_post(pre_order[index+2:length], post_order[index+1:length-1])

        return root



    @staticmethod
    def build_tree_llist(llist_node):
        if llist_node is None:
            return None
        currl = llist_node
        queue = Queue()
        root = Node(currl.data)
        curr = root
        currl = currl.next
        while currl is not None:
            if currl is None:
                return root
            curr.left_child = Node(currl.data)
            queue.put(curr.left_child)
            currl = currl.next
            if currl is None:
                return root
            curr.right_child = Node(currl.data)
            queue.put(curr.right_child)
            currl = currl.next
            curr = queue.get()
        return root

    @staticmethod
    def build_tree_in_level(in_order, level_order):
        if level_order is None or in_order is None or len(level_order) == 0:
            return None

        root = Node(level_order[0])
        index = in_order.index(level_order[0])
        length = len(level_order)
        root.left_child = Node.build_tree_in_level(in_order[0:index+1], [item for item in level_order if in_order.index(item) < index])
        root.right_child = Node.build_tree_in_level(in_order[index+1:length], [item for item in level_order if in_order.index(item) > index])

        return root

    @staticmethod
    def build_tree(pre_order, in_order):
        if pre_order is None or in_order is None or len(pre_order) == 0:
            return None

        root = Node(pre_order[0])
        index = in_order.index(pre_order[0])
        length = len(pre_order)
        root.left_child = Node.build_tree(pre_order[1:index+1], in_order[0:index])
        root.right_child = Node.build_tree(pre_order[index+1:length], in_order[index+1:length])

        return root

    def boundaries(self):

        def left(curr):
            if curr is None or (curr.left_child is None and curr.right_child is None):
                return ''
            if curr.left_child:
                return str(curr.data) + left(curr.left_child)
            else:
                return str(curr.data) + left(curr.right_child)

        def right(curr):
            if curr is None or (curr.left_child is None and curr.right_child is None):
                return ''
            if curr.right_child:
                return right(curr.right_child) + str(curr.data)
            else:
                return right(curr.left_child) + str(curr.data)

        def leaves(curr):
            if curr is None:
                return ''
            if curr.left_child is None and curr.right_child is None:
                return str(curr.data)
            else:
                return leaves(curr.left_child) + leaves(curr.right_child)

        curr = self
        return str(curr.data) + left(curr.left_child) + leaves(curr.left_child) + leaves(curr.right_child) + right(curr.right_child)

    def vertical_string(self):
        m = dict()
        hd = 0
        self.vertical_order_map(hd, m)

        res = ''
        for key, value in sorted(m.items()):
            for i in value:
                res = res + str(i)
        return res

    def vertical_order_map(self, hd, m):
        if m.get(hd):
            m[hd].append(self.data)
        else:
            m[hd] = [self.data]

        if self.left_child:
            self.left_child.vertical_order_map(hd-1, m)
        if self.right_child:
            self.right_child.vertical_order_map(hd+1, m)

    def vertical_print(self, line, hd):
        res = ''
        if hd == line:
            res = res + str(self.data)
        if self.left_child is not None:
            res = res + self.left_child.vertical_print(line, hd - 1)
        if self.right_child is not None:
            res = res + self.right_child.vertical_print(line, hd + 1)
        return res

    def vertical_order(self):
        min, max = self.find_leftmost_rightmost(0)

        res = ''
        for line in range(min, max+1):
            res = res + self.vertical_print(line, 0)

        return res

    def find_leftmost_rightmost(self, hd):
        lmin = lmax = rmin = rmax = hd
        if self.left_child:
            lmin, lmax = self.left_child.find_leftmost_rightmost(hd - 1)
        if self.right_child:
            rmin, rmax = self.right_child.find_leftmost_rightmost(hd + 1)

        return min(lmin, rmin), max(lmax, rmax)

    def get_leaves(self):
        if self.left_child is None and self.right_child is None:
            head = tail = DLLNode(self.data)
            return head, tail
        if self.left_child is not None:
            head, tail = self.left_child.get_leaves()
            if self.right_child is not None:
                rhead, rtail = self.right_child.get_leaves()
                tail.next = rhead
                tail = rtail
        else:
            head, tail = self.right_child.get_leaves()

        return head, tail

    def compare_leaves(self, treeb):
        head, tail = self.get_leaves()
        headb, tailb = treeb.get_leaves()
        dlla = DoublyLinkedList()
        dlla.head = head
        dllb = DoublyLinkedList()
        dllb.head = headb
        return dlla.compare(dllb)

    def to_dlinked_list(self):
        head = tail = node = DLLNode(self.data)
        if self.left_child is not None:
            head, ltail = self.left_child.to_dlinked_list()
            node.prev = ltail
            ltail.next = node
        if self.right_child is not None:
            rhead, tail = self.right_child.to_dlinked_list()
            node.next = rhead
            rhead.prev = node
        return head, tail

    def remove_node(self, value, parent):
        if value < self.data and self.left_child is not None:
            return self.left_child.remove_node(value, self)
        elif value < self.data:
            return False
        elif value > self.data and self.right_child is not None:
            return self.right_child.remove_node(value, self)
        elif value > self.data:
            return False
        else:
            if self.left_child is None and self.right_child is None:
                if self == parent.left_child:
                    parent.left_child = None
                else:
                    parent.right_child = None
            elif self.right_child is None:
                if self == parent.left_child:
                    parent.left_child = self.left_child
                else:
                    parent.right_child = self.left_child
            elif self.left_child is None:
                if self == parent.left_child:
                    parent.left_child = self.right_child
                else:
                    parent.right_child = self.right_child
            else:
                self.data = self.right_child.get_minimum_value()
                self.right_child.remove_node(self.data, self)
            return True

    def get_minimum_value(self):
        if self.left_child is None:
            return self.data
        return self.left_child.get_minimun_value()

    def binary_search(self, data):
        if self.data == data:
            return self
        if data < self.data:
            if self.left_child is not None:
                return self.left_child.binary_search(data)
            else:
                return None
        if data > self.data:
            if self.right_child is not None:
                return self.right_child.binary_search(data)
            else:
                return None

    def insert(self, data):
        if data <= self.data:
            self.insert_left(data)
        else:
            self.insert_right(data)

    def str_bfs(self):
        res = ''
        queue = Queue()
        queue.put(self)

        while not queue.empty():
            curr = queue.get()
            res = res + curr.data
            if curr.left_child is not None:
                queue.put(curr.left_child)
            if curr.right_child is not None:
                queue.put(curr.right_child)
        return res

    def str_post_order(self):
        res = ''
        if self.left_child is not None:
            res = res + self.left_child.str_post_order()
        if self.right_child is not None:
            res = res + self.right_child.str_post_order()
        res = res + str(self.data)
        return res

    def str_in_order(self):
        res = ''
        if self.left_child is not None:
            res = res + self.left_child.str_in_order()
        res = res + str(self.data)
        if self.right_child is not None:
            res = res + self.right_child.str_in_order()
        return res

    def str_pre_order(self):
        res = str(self.data)
        if self.left_child is not None:
            res = res + self.left_child.str_pre_order()
        if self.right_child is not None:
            res = res + self.right_child.str_pre_order()
        return res

    def insert_left(self, data):
        if self.left_child is not None:
            self.left_child.insert(data)
        else:
            child = Node(data)
            self.left_child = child

    def insert_right(self, data):
        if self.right_child is not None:
            self.right_child.insert(data)
        else:
            child = Node(data)
            self.right_child = child