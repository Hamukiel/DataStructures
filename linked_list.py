class Node:

    def __init__(self, data, child=None):
        self.data = data
        self.next = None
        self.child = child


class LinkedList:

    def __init__(self):
        self.head = None

    def count_rotations(self):
        curr = self.head
        rotations = 0
        min = curr.data
        while curr is not None:
            if min > curr.data:
                rotations += 1
            curr = curr.next
        return rotations

    def sort_012_inplace(self):
        prev = [None, None, None]
        first = [None, None, None, None]
        curr = self.head
        while curr is not None:
            if prev[curr.data] is not None:
                prev[curr.data].next = curr
            else:
                first[curr.data] = curr
            prev[curr.data] = curr
            curr = curr.next
        for i in range(0, 3):
            prev[i].next = first[i+1]
        self.head = first[0]

    def max_palindrome(self):
        def count_common(a, b):
            count = 0
            while a is not None and b is not None:
                if a.data == b.data:
                    count += 1
                else:
                    break
                a = a.next
                b = b.next
            return count

        result = 0
        prev = None
        curr = self.head
        while curr is not None:
            next = curr.next
            curr.next = prev
            result = max(result, 2*count_common(prev, next)+1)
            result = max(result, 2 * count_common(curr, next))
            prev = curr
            curr = next
        return result

    def swap_k(self, k):
        if k < 1:
            return
        prev = None
        first = None
        curr = self.head
        i = 1
        while curr is not None and i < k:
            prev = curr
            curr = curr.next
            i += 1

        if curr is None:
            return

        first = curr
        slow = self.head
        slow_prev = None

        while curr.next is not None:
            curr = curr.next
            slow_prev = slow
            slow = slow.next

        if slow == first:
            return

        slow_prev.next = first
        temp = slow.next
        slow.next = first.next
        first.next = temp
        if prev is None:
            self.head = slow
        else:
            prev.next = slow

    def delete_m_n(self, m, n):
        curr = self.head
        while curr is not None:
            i = 1
            while curr is not None and i < m:
                curr = curr.next
                i += 1

            if curr is None:
                return

            i = 0
            prev = curr
            while curr is not None and i <= n:
                curr = curr.next
                i = i+1

            prev.next = curr

    def multi_flatten(self):
        last = self.head
        while last.next is not None:
            last = last.next
        curr = self.head
        prev = last
        while curr is not None:
            if curr.child is not None:
                prev.next = curr.child
                while prev.next is not None:
                    prev = prev.next
            curr = curr.next

    def sort_0_1_2(self):
        count = [0, 0, 0]
        curr = self.head
        while curr is not None:
            count[curr.data] += 1
            curr = curr.next
        curr = self.head
        i = 0
        while curr is not None:
            if count[i] == 0:
                i += 1
            else:
                count[i] -= 1
                curr.data = i
                curr = curr.next

    def num_sum_list_alt(self, listb):
        res = LinkedList()

        def node_sum(nodeA, nodeB):
            if nodeA is None:
                return None, 0
            acc = 0
            result = Node(None)
            result.next, acc = node_sum(nodeA.next, nodeB.next)
            val = nodeA.data + nodeB.data + acc
            if val > 9:
                acc = 1
                val = val - 10
            result.data = val
            return result, acc

        def add_acc(node, curr, acc):
            if node != curr:
                acc = add_acc(node.next, curr, acc)
                sum = node.data + acc
                if sum > 9:
                    acc = 1
                    sum = sum - 10
                res.push(sum)
            return acc

        if self.head is None:
            res.head = listb.head
        if listb.head is None:
            res.head = self.head
        sizeA = self.count()
        sizeB = listb.count()
        if sizeA == sizeB:
            result, acc = node_sum(self.head, listb.head)
            res.head = result
            add_acc(res.head, res.head, acc)
        else:
            if sizeA > sizeB:
                diff = sizeA - sizeB
                big = self
                small = listb
            else:
                diff = sizeB - sizeA
                big = listb
                small = self
            i = 0
            curr = big.head
            while i < diff:
                curr = curr.next
                i = i+1
            result, acc = node_sum(curr, small.head)
            res.head = result
            acc = add_acc(big.head, curr, acc)
        if acc == 1:
            res.push(1)
        return res

    def flatten(self):
        curr = self.head
        while curr is not None and curr.next is not None:
            curr.data.sorted_merge(curr.next.data)
            curr.next = curr.next.next
        self.head = curr.data.head

    def rotate(self, k):
        if k < 1:
            return
        curr = self.head
        i = 1
        while curr is not None and i < k:
            curr = curr.next
            i = i+1

        if curr is None:
            return

        temp = curr.next
        curr.next = None
        curr = self.head
        self.head = temp

        while temp.next is not None:
            temp = temp.next

        temp.next = curr

    def triplet_sum(self, listb, listc, number):
        curr = self.head
        listb.merge_sort()
        listc.merge_sort()
        listc.reverse()
        while curr is not None:
            currb = listb.head
            currc = listc.head
            while currb is not None and currc is not None:
                sum = curr.data + currb.data + currc.data
                if sum == number:
                    return curr.data, currb.data, currc.data
                if sum < number:
                    currb = currb.next
                else:
                    currc = currc.next
            curr = curr.next
        return None

    def union_intersection(self, listb):
        hash = set()
        union = LinkedList()
        intersection = LinkedList()
        curr = self.head
        currb = listb.head
        while curr is not None:
            if curr.data not in hash:
                hash.add(curr.data)
                union.append(curr.data)
            curr = curr.next
        while currb is not None:
            if currb.data in hash:
                intersection.append(currb.data)
            else:
                union.append(currb.data)
            currb = currb.next
        return union, intersection

    def delete_from(self, node, n):
        if node == n:
            if node.next is not None:
                node.data = node.next.data
                node.next = node.next.next
        prev = node
        while prev is not None and prev.next is not None:
            prev = prev.next

        if prev.next is None:
            return

        prev.next = prev.next.next

    def detect_and_remove_loop(self):
        hash = set()
        curr = self.head
        prev = None
        while curr is not None:
            if curr not in hash:
                hash.add(curr)
                prev = curr
                curr = curr.next
            else:
                prev.next = None
                curr = prev.next

    def num_list_sum(self, listb):
        res = LinkedList()
        curr = self.head
        currb = listb.head
        acc = 0
        while curr is not None or currb is not None or acc > 0:
            if curr is not None:
                curr_value = curr.data
                curr = curr.next
            else:
                curr_value = 0
            if currb is not None:
                currb_value = currb.data
                currb = currb.next
            else:
                currb_value = 0
            sum = curr_value + currb_value + acc
            acc = 0
            if sum > 9:
                sum = sum - 10
                acc = 1
            res.append(sum)
        return res

    def segregate_even_odd(self):
        even_dummy = Node(None)
        odd_dummy = Node(None)
        even_prev = even_dummy
        odd_prev = odd_dummy
        curr = self.head
        while curr is not None:
            if curr.data % 2 == 0:
                even_prev.next = curr
                even_prev = curr
            else:
                odd_prev.next = curr
                odd_prev = curr
            curr = curr.next
        even_prev.next = odd_dummy.next
        odd_prev.next = None
        self.head = even_dummy.next

    def delete_descending(self):
        curr = self.head
        dummy = Node(None)
        prev = dummy
        prev.next = curr
        while curr is not None and curr.next is not None:
            if curr.data < curr.next.data:
                prev.next = curr.next
            else:
                prev = prev.next
            curr = curr.next
        self.head = dummy.next

    def alternate_k_reverse(self, k):
        if k < 1:
            return
        curr = self.head
        dummy = Node(None)
        prev = dummy
        i = 1
        ks = 0
        temp_list = LinkedList()
        temp_list.head = curr
        while curr is not None:
            if i == k:
                if (ks % 2) == 0:
                    temp_node = curr.next
                    curr.next = None
                    last = temp_list.head
                    temp_list.reverse()
                    prev.next = temp_list.head
                    last.next = temp_node
                    curr = temp_node
                    prev = last
                else:
                    prev = curr
                    curr = curr.next
                    temp_list.head = curr
                i = 1
                ks = ks + 1
            else:
                curr = curr.next
                i = i + 1
        self.head = dummy.next

    def k_reverse(self, k):
        if k < 1:
            return
        curr = self.head
        dummy = Node(None)
        prev = dummy
        i = 1
        temp_list = LinkedList()
        temp_list.head = curr
        while curr is not None:
            if i == k:
                temp_node = curr.next
                curr.next = None
                last = temp_list.head
                temp_list.reverse()
                prev.next = temp_list.head
                last.next = temp_node
                curr = temp_node
                temp_list.head = temp_node
                prev = last
                i = 1
            else:
                curr = curr.next
                i = i+1
        self.head = dummy.next

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
        a = LinkedList()
        b = LinkedList()
        if self.head is None:
            return a, b
        ref = self.head
        fref = self.head
        prev = None
        while fref is not None and fref.next is not None:
            prev = ref
            ref = ref.next
            fref = fref.next.next
        a.head = self.head
        b.head = ref
        prev.next = None
        return a, b

    def alternate_split(self):
        a = LinkedList()
        b = LinkedList()
        curr = self.head
        if self.head is None:
            return a, b
        icurr = self.head.next
        a.head = curr
        b.head = icurr
        while curr is not None and curr.next is not None:
            curr.next = curr.next.next
            if icurr.next is not None:
                icurr.next = icurr.next.next
                icurr = icurr.next
            curr = curr.next
        return a, b

    def delete_alternate(self):
        curr = self.head
        while curr is not None and curr.next is not None:
            curr.next = curr.next.next
            curr = curr.next

    def get_sorted_intersection(self, listb):
        res = LinkedList()
        if self.head is None or listb.head is None:
            return res
        curr = self.head
        currb = listb.head
        while curr is not None and currb is not None:
            if curr.data == currb.data:
                res.append(curr.data)
                curr = curr.next
                currb = currb.next
            else:
                if curr.data < currb.data:
                    curr = curr.next
                else:
                    currb = currb.next
        return res

    def last_to_first(self):
        curr = self.head
        prev = None
        while curr.next is not None:
            prev = curr
            curr = curr.next
        if prev is None:
            return
        curr.next = self.head
        prev.next = None
        self.head = curr

    def pairwise_swap(self):
        curr = self.head
        dummy = Node(None)
        prev = dummy
        while curr is not None and curr.next is not None:
            tmp = curr.next
            curr.next = tmp.next
            tmp.next = curr
            prev.next = tmp
            prev = curr
            curr = curr.next
        self.head = dummy.next

    def remove_duplicates(self):
        curr = self.head
        prev = None
        hash = set()
        while curr is not None:
            if curr.data in hash:
                prev.next = curr.next
            else:
                hash.add(curr.data)
                prev = curr
            curr = curr.next

    def sorted_remove_duplicates(self):
        curr = self.head
        while curr is not None:
            while curr.next is not None and curr.data == curr.next.data:
                curr.next = curr.next.next
            curr = curr.next

    def print_reverse(self):
        def aux_print(node):
            if node is None:
                return ''
            return aux_print(node.next) + str(node.data)

        return aux_print(self.head)

    def get_intersection(self, listb):
        hash = set()
        curr = self.head
        while curr is not None:
            hash.add(curr)
            curr = curr.next
        curr = listb.head
        while curr:
            if curr in hash:
                return curr
            curr = curr.next
        return None

    def is_palindrome(self):
        ref = self.head
        fref = self.head
        prev = self.head
        mid = None
        while fref is not None and fref.next is not None:
            fref = fref.next.next
            prev = ref
            ref = ref.next

        mid = ref
        if fref is not None:
            ref = ref.next

        temp_b = LinkedList()
        temp_b.head = ref
        prev.next = None
        temp_b.reverse()
        res = self.equals(temp_b)
        temp_b.reverse()
        prev.next = mid

        return res

    def equals(self, listB):
        curr = self.head
        currB = listB.head
        while curr is not None and currB is not None:
            if curr.data != currB.data:
                return False
            curr = curr.next
            currB = currB.next
        if curr != currB:
            return False
        return True

    def sorted_merge(self, listB):
        if self.head is None:
            self.head = listB.head
            return
        if listB.head is None:
            return
        currSelf = self.head
        currB = listB.head
        dest = Node(None)
        prev = dest
        while currSelf is not None and currB is not None:
            if currSelf.data <= currB.data:
                prev.next = currSelf
                currSelf = currSelf.next
            else:
                prev.next = currB
                currB = currB.next
            prev = prev.next
        if currSelf is None:
            prev.next = currB
        else:
            prev.next = currSelf
        self.head = dest.next

    def detect_loop(self):
        s = set()
        curr = self.head

        while curr:
            if curr in s:
                return True
            s.add(curr)
            curr = curr.next

        return False

    def reverse(self):
        curr = self.head
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    def occurrences(self, data):
        curr = self.head
        count = 0
        while curr:
            if curr.data == data:
                count = count+1
            curr = curr.next
        return count

    def clear(self):
        current = self.head
        while current:
            prev = current.next
            del current.data
            current = prev
        self.head = current

    def reverse_index(self, index):
        curr = self.head
        ref = self.head
        i = 0

        while ref and i <= index:
            ref = ref.next
            i = i+1

        while ref:
            curr = curr.next
            ref = ref.next

        return curr.data

    def get_middle(self):
        curr = self.head
        fast = self.head
        while fast and fast.next:
            curr = curr.next
            fast = fast.next.next

        return curr.data

    def swap(self, data1, data2):
        if data1 == data2:
            return
        current = self.head
        node1 = None
        node2 = None
        prev1 = None
        prev2 = None
        while (current is not None) and ((node1 is None) or (node2 is None)):
            if node1 is None:
                if current.data == data1:
                    node1 = current
                else:
                    prev1 = current
            if node2 is None:
                if current.data == data2:
                    node2 = current
                else:
                    prev2 = current
            current = current.next

        if (node1 is None) or (node2 is None):
            return

        if prev1 is not None:
            prev1.next = node2
        else:
            self.head = node2

        if prev2 is not None:
            prev2.next = node1
        else:
            self.head = node1

        temp = node1.next
        node1.next = node2.next
        node2.next = temp

    def contains(self, data):
        node = self.head
        while node:
            if node.data == data:
                return True
            node = node.next

        return False

    def get_node(self, data):
        if self.head is None:
            return None

        node = self.head
        while node:
            if node.data == data:
                return node
            node = node.next

        return None

    def get_node_at(self, index):
        if index < 0 or self.head is None:
            return None

        i = 0
        node = self.head
        while node:
            if i == index:
                return node
            node = node.next
            i = i+1

        return None

    def get_index(self, data):
        if self.head is None:
            return None

        node = self.head
        index = 0
        while node:
            if node.data == data:
                return index
            node = node.next
            index = index + 1

        return None

    def push(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

    def insert_after(self, prev_data, data):
        node = self.get_node(prev_data)

        new = Node(data)
        new.next = node.next
        node.next = new

    def append(self, data):
        new = Node(data)

        if self.head is None:
            self.head = new
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new

    def delete(self, key):
        if self.head is None:
            return

        prev = self.head
        if prev.data == key:
            self.head = prev.next
            return

        while prev.next:
            if prev.next.data == key:
                prev.next = prev.next.next
                return
            prev = prev.next

    def delete_at(self, index):

        if index < 0:
            return

        if index == 0:
            self.head = self.head.next
            return

        prev = self.head
        i = 1
        while prev.next:
            if i == index:
                prev.next = prev.next.next
                return
            prev = prev.next
            i = i+1

    def count(self):
        i = 0;
        node = self.head
        while node:
            i = i+1
            node = node.next
        return i

    def __str__(self):
        res = ''
        temp = self.head
        while temp:
            res = res + str(temp.data)
            temp = temp.next
        return res

    def print(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next