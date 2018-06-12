class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        self.random = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def __str__(self):
        res = ''
        curr = self.head
        while curr is not None:
            res = res + str(curr.data)+' '
            curr = curr.next
        return res

    def compare(self, dllb):

        curr = self.head
        currb = dllb.head

        while curr is not None and currb is not None:
            if curr.data != currb.data:
                return False
            curr = curr.next
            currb = currb.next

        if curr != currb:
            return False

        return True

    def partition(self, lnode, hnode):
        x = hnode.data
        if lnode.prev is not None:
            prev = lnode.prev
            bprev = False
        else:
            prev = Node(None)
            prev.next = lnode
            lnode.prev = prev
            bprev = True
        if hnode.next is not None:
            next = hnode.next
            bnext = False
        else:
            bnext = True
            next = Node(None)
            next.prev = hnode
            hnode.next = next
        nodei = prev
        nodej = lnode
        while nodej != hnode:
            temp = nodej.next
            if nodej.data <= x:
                nodei = nodei.next
                self.swap(nodei, nodej)
                nodei = nodej
            nodej = temp
        nodei = nodei.next
        self.swap(nodei, hnode)
        nodei = hnode
        if bprev:
            prev.next.prev = None
        if bnext:
            next.prev.next = None
        return nodei, prev.next, next.prev

    def quick_sort(self):
        def sort(nodel, nodeh):
            if nodeh is not None and nodel != nodeh and nodel != nodeh.next:
                temp, head, tail = self.partition(nodel, nodeh)
                head = sort(head, temp.prev)
                sort(temp.next, tail)
                return head
            return nodel

        if self.head is None or self.head.next is None:
            return
        tail = self.get_last()
        self.head = sort(self.head, tail)

    def swap(self, node_a, node_b):
        if node_a == node_b or node_a is None or node_b is None:
            return

        temp = node_b.prev

        if node_a.prev != node_b:
            if node_a.prev is not None:
                node_a.prev.next = node_b
            else:
                self.head = node_b
            node_b.prev = node_a.prev
        else:
            node_b.prev = node_a

        if temp != node_a:
            if temp is not None:
                temp.next = node_a
            else:
                self.head = node_a
            node_a.prev = temp
        else:
            node_a.prev = node_b

        temp = node_b.next
        if node_a.next != node_b:
            if node_a.next is not None:
                node_a.next.prev = node_b
            node_b.next = node_a.next
        else:
            node_b.next = node_a

        if temp != node_a:
            if temp is not None:
                temp.prev = node_a
            node_a.next = temp
        else:
            node_a.next = node_b

    def get_last(self):
        if self.head is None:
            return None
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        return curr

    def sorted_insert(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        curr = self.head
        while curr is not None:
            if curr.data >= data:
                self.insert_before(data, curr)
                return
            curr = curr.next
        self.append(data)

    def merge_sort(self):
        if self.head is None or self.head.next is None:
            return self
        a, b = self.split()
        a.merge_sort()
        b.merge_sort()
        a.sorted_merge(b)
        self.head = a.head
        return self

    def split(self):
        a = DoublyLinkedList()
        b = DoublyLinkedList()
        if self.head is None:
            return a, b
        ref = self.head
        fref = self.head
        while fref is not None and fref.next is not None:
            ref = ref.next
            fref = fref.next.next
        a.head = self.head
        b.head = ref
        if ref.prev is not None:
            ref.prev.next = None
            ref.prev = None
        return a, b

    def sorted_merge(self, llistb):
        if self.head is None:
            self.head = llistb.head
            return
        if llistb.head is None:
            return
        dummy = Node(None)
        prev = dummy
        curr = self.head
        currb = llistb.head
        while curr is not None and currb is not None:
            if curr.data <= currb.data:
                prev.next = curr
                curr.prev = prev
                curr = curr.next
            else:
                prev.next = currb
                currb.prev = prev
                currb = currb.next
            prev = prev.next
        if curr is None and currb is not None:
            prev.next = currb
            currb.prev = prev
        elif curr is not None and currb is None:
            prev.next = curr
            curr.prev = prev
        self.head = dummy.next
        self.head.prev = None

    def clone_random(self):
        curr = self.head

        while curr is not None:
            temp = curr.next
            curr.next = Node(curr.data)
            curr.next.next = temp
            curr = temp

        curr = self.head

        while curr is not None:
            curr.next.random = curr.random.next
            curr = curr.next.next

        curr = self.head

        res = DoublyLinkedList()
        res.head = curr.next
        copy = res.head

        while curr is not None and copy is not None:
            curr.next = copy.next
            if copy.next is None:
                copy.next = None
            else:
                copy.next = copy.next.next
            curr = curr.next
            copy = copy.next
        return res

    def reverse(self):
        if self.head is None:
            return
        temp = None
        curr = self.head
        while curr is not None:
            temp = curr.prev
            curr.prev = curr.next
            curr.next = temp
            curr = curr.prev
        self.head = temp.prev

    def delete_node(self, node):
        if node is None or self.head is None:
            return
        if node == self.head:
            self.head = node.next
        if node.next is not None:
            node.next.prev = node.prev
        if node.prev is not None:
            node.prev.next = node.next

    def push(self, data):
        node = Node(data)
        if self.head is not None:
            self.head.prev = node
        node.next = self.head
        self.head = node

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = node
            node.prev = curr

    def insert_after(self, data, node):
        if node is None:
            self.push(data)
        else:
            new = Node(data)
            new.next = node.next
            new.prev = node
            node.next = new
            if new.next is not None:
                new.next.prev = new

    def insert_before(self, data, node):
        new = Node(data)
        new.next = node
        new.prev = node.prev
        node.prev = new
        if new.prev is not None:
            new.prev.next = new
        else:
            self.head = new
