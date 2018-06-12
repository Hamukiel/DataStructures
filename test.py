from linked_list import LinkedList, Node
import unittest


class LinkedListTests(unittest.TestCase):

    def test_push(self):
        llist = LinkedList()
        llist.push(1)
        llist.push(2)
        llist.push(3)
        llist.push(4)
        self.assertEqual(str(llist), '4321')

    def test_append(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        llist.append(4)
        self.assertEqual(str(llist), '1234')

    def test_get_node(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        llist.append(4)
        self.assertEqual(llist.get_node(3).data, 3)

    def test_get_index(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        llist.append(4)
        self.assertEqual(llist.get_index(3), 2)

    def test_get_node_at(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        llist.append(4)
        self.assertEqual(llist.get_node_at(2).data, 3)

    def test_insert_after(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        llist.append(4)
        llist.insert_after(2, 2.5)
        self.assertEqual(str(llist), '122.534')

    def test_delete(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        llist.append(4)
        llist.delete(2)
        self.assertEqual(str(llist), '134')

    def test_delete_at(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        llist.append(4)
        llist.delete_at(2)
        self.assertEqual(str(llist), '124')

    def test_count(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        llist.append(4)
        self.assertEqual(llist.count(), 4)

    def test_Swap(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        llist.append(4)
        llist.swap(2,3)
        self.assertEqual(str(llist), '1324')

    def test_middle(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        llist.append(4)
        llist.append(5)
        self.assertEqual(llist.get_middle(), 3)

    def test_reverse_index(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        llist.append(4)
        llist.append(5)
        self.assertEqual(llist.reverse_index(4), 1)

    def test_clear(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        llist.append(4)
        llist.append(5)
        llist.clear()
        self.assertIsNone(llist.head)

    def test_occurrences(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(1)
        llist.append(4)
        llist.append(1)
        self.assertEqual(llist.occurrences(1), 3)

    def test_reverse(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        llist.append(4)
        llist.append(5)
        llist.reverse()
        self.assertEqual(str(llist), '54321')

    def test_detect_loop(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        llist.append(4)
        llist.append(5)
        llist.head.next.next.next.next.next = llist.head
        self.assertTrue(llist.detect_loop())

    def test_sorted_merge(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(3)
        llist.append(5)
        llist.append(7)
        llist.append(11)

        llistb = LinkedList()
        llistb.append(2)
        llistb.append(3)
        llistb.append(4)
        llistb.append(5)
        llistb.append(9)
        llistb.append(10)
        llistb.append(15)
        llist.sorted_merge(llistb)
        self.assertEqual(str(llist), '123345579101115')

    def test_compare(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        llist.append(4)
        llist.append(5)

        llist2 = LinkedList()
        llist2.append(1)
        llist2.append(2)
        llist2.append(3)
        llist2.append(4)
        llist2.append(5)

        self.assertTrue(llist.equals(llist2))

    def test_palindrome(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        llist.append(2)
        llist.append(1)
        self.assertTrue(llist.is_palindrome())

    def test_insersection(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        llist.append(4)
        llist.append(5)

        llist2 = LinkedList()
        llist2.head = llist.head.next.next
        llist2.push(8)
        llist2.push(7)
        llist2.push(6)
        self.assertEqual(llist.get_intersection(llist2).data, 3)

    def test_print_reverse(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        llist.append(4)
        llist.append(5)
        self.assertEqual(llist.print_reverse(), '54321')

    def test_sorted_remove_duplicates(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(1)
        llist.append(1)
        llist.append(1)
        llist.append(1)
        llist.append(1)
        llist.append(1)
        llist.append(2)
        llist.append(3)
        llist.append(3)
        llist.append(4)
        llist.append(5)
        llist.append(5)
        llist.append(5)
        llist.sorted_remove_duplicates()
        self.assertEqual(str(llist), '12345')

    def test_remove_duplicates(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(5)
        llist.append(3)
        llist.append(3)
        llist.append(1)
        llist.append(2)
        llist.append(1)
        llist.append(1)
        llist.append(5)
        llist.append(1)
        llist.append(4)
        llist.append(5)
        llist.append(1)
        llist.append(1)
        llist.remove_duplicates()
        self.assertEqual(str(llist), '15324')

    def test_pairwise_swap(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        llist.append(4)
        llist.append(5)
        llist.append(6)
        llist.pairwise_swap()
        self.assertEqual(str(llist), '214365')

    def test_last_to_first(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        llist.append(4)
        llist.append(5)
        llist.last_to_first()
        self.assertEqual(str(llist), '51234')

    def test_sorted_intersection(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        llist.append(4)
        llist.append(5)
        llistb = LinkedList()
        llistb.append(1)
        llistb.append(3)
        llistb.append(5)
        llistb.append(6)
        llistb.append(7)
        llistc = llist.get_sorted_intersection(llistb)
        self.assertEqual(str(llistc), '135')

    def test_delete_alternate(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        llist.append(4)
        llist.delete_alternate()
        self.assertEqual(str(llist), '13')

    def test_alternate_split(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        llist.append(4)
        llist.append(5)
        llist.append(6)
        a, b = llist.alternate_split()
        self.assertEqual(str(a), '135')
        self.assertEqual(str(b), '246')

    def test_merge_sort(self):
        llist = LinkedList()
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
        self.assertEqual(str(llist), '1234567911234152')

    def test_k_reverse(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        llist.append(4)
        llist.append(5)
        llist.append(6)
        llist.append(7)
        llist.append(8)
        llist.append(9)
        llist.k_reverse(2)
        self.assertEqual(str(llist), '214365879')

    def test_k_reverse(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        llist.append(4)
        llist.append(5)
        llist.append(6)
        llist.append(7)
        llist.append(8)
        llist.append(9)
        llist.alternate_k_reverse(3)
        self.assertEqual(str(llist), '321456987')

    def test_delete_descending(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(22)
        llist.append(13)
        llist.append(14)
        llist.append(5)
        llist.append(6)
        llist.append(71)
        llist.append(8)
        llist.append(9)
        llist.delete_descending()
        self.assertEqual(str(llist), '2214719')

    def test_segregate_even_odd(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        llist.append(4)
        llist.append(5)
        llist.append(6)
        llist.append(7)
        llist.append(8)
        llist.append(9)
        llist.segregate_even_odd()
        self.assertEqual(str(llist), '246813579')

    def test_detect_and_remove_loop(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        llist.append(4)
        llist.append(5)
        llist.head.next.next.next.next.next = llist.head.next.next
        self.assertTrue(llist.detect_loop())
        llist.detect_and_remove_loop()
        self.assertFalse(llist.detect_loop())

    def test_num_list_sum(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        llistb = LinkedList()
        llistb.append(4)
        llistb.append(5)
        llistb.append(9)
        llistb.append(2)
        llistb.append(3)
        llistb.append(1)
        res = llist.num_list_sum(llistb)
        self.assertEqual(str(res), '572331')

    def test_union_intersection(self):
        llist = LinkedList()
        llist.append(10)
        llist.append(15)
        llist.append(4)
        llist.append(20)
        llistb = LinkedList()
        llistb.append(8)
        llistb.append(4)
        llistb.append(2)
        llistb.append(10)
        union, intersection = llist.union_intersection(llistb)
        self.assertEqual(str(union), '101542082')
        self.assertEqual(str(intersection), '410')

    def test_triplet_sum(self):
        llist = LinkedList()
        llistb = LinkedList()
        llistc = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        llist.append(4)
        llistb.append(5)
        llistb.append(6)
        llistb.append(7)
        llistb.append(8)
        llistc.append(9)
        llistc.append(10)
        llistc.append(11)
        llistc.append(12)
        a, b, c = llist.triplet_sum(llistb, llistc, 24)
        self.assertEqual((a, b, c), (4, 8, 12))

    def test_rotate(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        llist.append(4)
        llist.append(5)
        llist.append(6)
        llist.rotate(3)
        self.assertEqual(str(llist), '456123')

    def test_flatten(self):
        llist = LinkedList()
        a = LinkedList()
        a.append(2)
        a.append(5)
        a.append(7)
        b = LinkedList()
        b.append(3)
        b.append(6)
        b.append(8)
        c = LinkedList()
        c.append(5)
        c.append(7)
        c.append(9)
        d = LinkedList()
        d.append(6)
        d.append(8)
        d.append(11)
        llist.append(a)
        llist.append(b)
        llist.append(c)
        llist.append(d)
        llist.flatten()
        self.assertEqual(str(llist), '2355667788911')

    def test_num_sum_list_alt(self):
        llist = LinkedList()
        llist.append(9)
        llist.append(9)
        llist.append(9)
        llist.append(9)
        llist.append(9)
        llistb = LinkedList()
        llistb.append(9)
        llistb.append(9)
        llistb.append(9)
        llistc = llist.num_sum_list_alt(llistb)
        self.assertEqual(str(llistc), '100998')

    def test_count_012(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(2)
        llist.append(2)
        llist.append(1)
        llist.append(1)
        llist.append(0)
        llist.append(0)
        llist.append(0)
        llist.sort_0_1_2()
        self.assertEqual(str(llist), '000111222')

    def test_multi_flatten(self):
        llist = LinkedList()
        node1 = Node(10)
        node11 = Node(4)
        node12 = Node(20)
        node121 = Node(2)
        node13 = Node(13)
        node131 = Node(16)
        node1311 = Node(3)
        node2 = Node(5)
        node3 = Node(12)
        node4 = Node(7)
        node41 = Node(17)
        node411 = Node(9)
        node4111 = Node(19)
        node4112 = Node(15)
        node412 = Node(8)
        node42 = Node(6)
        node5 = Node(11)
        node1.child = node11
        node11.next = node12
        node12.child = node121
        node12.next = node13
        node13.child = node131
        node131.child = node1311
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5
        node4.child = node41
        node41.next = node42
        node41.child = node411
        node411.next = node412
        node411.child = node4111
        node4111.next = node4112
        llist.head = node1
        llist.multi_flatten()
        self.assertEqual(str(llist), '10512711420131762169831915')

    def test_delete_mn(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        llist.append(4)
        llist.append(5)
        llist.append(6)
        llist.append(7)
        llist.append(8)
        llist.append(9)
        llist.append(10)
        llist.delete_m_n(3, 2)
        self.assertEqual(str(llist), '123678')

    def test_swap_k(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        llist.append(4)
        llist.append(5)
        llist.append(6)
        llist.append(7)
        llist.append(8)
        llist.append(9)
        llist.append(10)
        llist.swap_k(3)
        self.assertEqual(str(llist), '12845673910')

    def test_max_palindrome(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        llist.append(2)
        llist.append(1)
        llist.append(2)
        llist.append(1)
        llist.append(1)
        llist.append(1)
        llist.append(10)
        self.assertEqual(llist.max_palindrome(), 5)

    def test_sort_012_inplace(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(2)
        llist.append(2)
        llist.append(1)
        llist.append(1)
        llist.append(0)
        llist.append(0)
        llist.append(0)
        llist.sort_012_inplace()
        self.assertEqual(str(llist), '000111222')

    def test_count_rotations(self):
        llist = LinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        llist.append(4)
        llist.append(5)
        llist.append(6)
        llist.append(7)
        llist.append(8)
        llist.append(9)
        llist.rotate(3)
        self.assertEqual(3, llist.count_rotations())