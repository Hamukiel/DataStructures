from src.doubly_linked_list import DoublyLinkedList, Node
import unittest


class DoublyLinkedListTests(unittest.TestCase):

    def test_push(self):
        llist = DoublyLinkedList()
        llist.push(5)
        llist.push(4)
        llist.push(3)
        llist.push(2)
        llist.push(1)
        self.assertEqual('1 2 3 4 5 ', str(llist))

    def test_append(self):
        llist = DoublyLinkedList()
        llist.append(5)
        llist.append(4)
        llist.append(3)
        llist.append(2)
        llist.append(1)
        self.assertEqual('5 4 3 2 1 ', str(llist))

    def test_insert_after(self):
        llist = DoublyLinkedList()
        llist.push(4)
        llist.push(2)
        llist.insert_after(5, llist.head.next)
        llist.insert_after(3, llist.head)
        self.assertEqual('2 3 4 5 ', str(llist))

    def test_insert_before(self):
        llist = DoublyLinkedList()
        llist.push(4)
        llist.push(2)
        llist.insert_before(3, llist.head.next)
        llist.insert_before(1, llist.head)
        self.assertEqual('1 2 3 4 ', str(llist))

    def test_delete_node(self):
        llist = DoublyLinkedList()
        llist.push(5)
        llist.push(4)
        llist.push(3)
        llist.push(2)
        llist.push(1)
        llist.delete_node(llist.head.next)
        self.assertEqual('1 3 4 5 ', str(llist))

    def test_reverse(self):
        llist = DoublyLinkedList()
        llist.push(5)
        llist.push(4)
        llist.push(3)
        llist.push(2)
        llist.push(1)
        llist.reverse()
        self.assertEqual('5 4 3 2 1 ', str(llist))

    def test_clone_random(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node5 = Node(5)
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5
        node1.random = node3
        node2.random = node1
        node3.random = node5
        node4.random = node5
        node5.random = node1
        llist = DoublyLinkedList()
        llist.head = node1
        lcopy = llist.clone_random()
        self.assertEqual(str(llist), str(lcopy))
        self.assertTrue(lcopy.head.random.data == llist.head.random.data)
        self.assertTrue(lcopy.head.next.random.data == llist.head.next.random.data)
        self.assertTrue(lcopy.head.next.next.random.data == llist.head.next.next.random.data)
        self.assertTrue(lcopy.head.next.next.next.random.data == llist.head.next.next.next.random.data)
        self.assertTrue(lcopy.head.next.next.next.next.random.data == llist.head.next.next.next.next.random.data)

    def test_merge_sort(self):
        llist = DoublyLinkedList()
        llist.append(7)
        llist.append(3)
        llist.append(52)
        llist.append(1)
        llist.append(5)
        llist.append(2)
        llist.append(11)
        llist.append(4)
        llist.append(41)
        llist.append(6)
        llist.append(9)
        llist.append(23)
        llist.merge_sort()
        self.assertEqual(str(llist), '1 2 3 4 5 6 7 9 11 23 41 52 ')

    def test_swap(self):
        llist = DoublyLinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        llist.append(4)
        llist.append(5)
        llist.append(6)
        llist.append(7)
        llist.append(8)
        llist.append(9)
        llist.swap(llist.head, llist.get_last())
        llist.swap(llist.head.next.next, llist.get_last().prev.prev)
        llist.swap(llist.head.next, llist.head.next.next)
        llist.swap(llist.head.next.next, llist.head.next.next.next)
        llist.swap(llist.head.next.next.next, llist.head.next.next.next.next)
        llist.swap(llist.head.next.next, llist.head.next.next.next)
        self.assertEqual(str(llist), '9 7 5 4 2 6 3 8 1 ')

    def test_quick_sort(self):
        llist = DoublyLinkedList()
        llist.append(7)
        llist.append(3)
        llist.append(52)
        llist.append(1)
        llist.append(5)
        llist.append(2)
        llist.append(11)
        llist.append(4)
        llist.append(41)
        llist.append(6)
        llist.append(9)
        llist.append(23)
        llist.quick_sort()
        self.assertEqual(str(llist), '1 2 3 4 5 6 7 9 11 23 41 52 ')

    def test_compare(self):
        llist = DoublyLinkedList()
        llist.append(7)
        llist.append(3)
        llist.append(52)
        llist.append(1)
        llist.append(5)
        llist.append(2)
        llistb = DoublyLinkedList()
        llistb.append(7)
        llistb.append(3)
        llistb.append(52)
        llistb.append(1)
        llistb.append(5)
        llistb.append(2)
        self.assertTrue(llist.compare(llistb))
        llistb.append(15)
        self.assertFalse(llist.compare(llistb))
