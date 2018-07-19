from src.binary_tree import Node
from src.doubly_linked_list import DoublyLinkedList
from src.linked_list import LinkedList
import unittest


class BinaryTreeTests(unittest.TestCase):

    def test_str(self):
        root = Node('a')
        root.insert_left('b')
        root.left_child.insert_right('d')
        root.insert_right('f')
        root.insert_right('c')
        root.right_child.insert_left('e')
        self.assertEqual('bdaecf', root.str_in_order())
        self.assertEqual('abdcef', root.str_pre_order())
        self.assertEqual('dbefca', root.str_post_order())
        self.assertEqual('abcdef', root.str_bfs())

    def test_insert(self):
        root = Node(50)
        root.insert(13)
        root.insert(21)
        root.insert(27)
        root.insert(76)
        root.insert(2)
        root.insert(44)
        root.insert(51)
        root.insert(6)
        root.insert(9)
        root.insert(11)
        self.assertEqual('2691113212744505176', root.str_in_order())

    def test_binary_search(self):
        root = Node(50)
        root.insert(13)
        root.insert(21)
        root.insert(27)
        root.insert(76)
        root.insert(2)
        root.insert(44)
        root.insert(51)
        root.insert(6)
        root.insert(9)
        root.insert(11)
        node = root.binary_search(10)
        self.assertIsNone(node)

    def test_to_dlinked_list(self):
        root = Node(10)
        root.left_child = Node(12)
        root.left_child.left_child = Node(25)
        root.left_child.right_child = Node(30)
        root.right_child = Node(15)
        root.right_child.left_child = Node(36)
        self.assertEqual('251230103615', root.str_in_order())
        dll = DoublyLinkedList()
        dll.head, temp = root.to_dlinked_list()
        self.assertEqual('25 12 30 10 36 15 ', str(dll))

    def test_compare_leaves(self):
        rootA = Node(1)
        rootA.left_child = Node(2)
        rootA.left_child.left_child = Node(4)
        rootA.right_child = Node(3)
        rootA.right_child.left_child = Node(6)
        rootA.right_child.right_child = Node(7)

        rootB = Node(0)
        rootB.left_child = Node(5)
        rootB.left_child.right_child = Node(4)
        rootB.right_child = Node(8)
        rootB.right_child.left_child = Node(6)
        rootB.right_child.right_child = Node(7)

        self.assertTrue(rootA.compare_leaves(rootB))

        rootC = Node(0)
        rootC.left_child = Node(1)
        rootC.left_child.left_child = Node(8)
        rootC.left_child.right_child = Node(9)
        rootC.right_child = Node(2)

        rootD = Node(1)
        rootD.left_child = Node(4)
        rootD.left_child.right_child = Node(8)
        rootD.right_child = Node(3)
        rootD.right_child.left_child = Node(2)
        rootD.right_child.right_child = Node(9)

        self.assertFalse(rootC.compare_leaves(rootD))

    def test_find_leftmost_rightmost(self):
        root = Node(10)
        root.left_child = Node(12)
        root.left_child.left_child = Node(25)
        root.left_child.right_child = Node(30)
        root.right_child = Node(15)
        root.right_child.left_child = Node(36)
        left, right = root.find_leftmost_rightmost(0)
        self.assertEqual(left, -2)
        self.assertEqual(right, 1)

    def test_vertical_order(self):
        root = Node(10)
        root.left_child = Node(12)
        root.left_child.left_child = Node(25)
        root.left_child.right_child = Node(30)
        root.right_child = Node(15)
        root.right_child.left_child = Node(36)
        self.assertEqual('251210303615', root.vertical_order())

    def test_vertical_string(self):
        root = Node(10)
        root.left_child = Node(12)
        root.left_child.left_child = Node(25)
        root.left_child.right_child = Node(30)
        root.right_child = Node(15)
        root.right_child.left_child = Node(36)
        self.assertEqual('251210303615', root.vertical_string())

    def test_boundaries(self):
        root = Node(10)
        root.left_child = Node(12)
        root.left_child.left_child = Node(25)
        root.left_child.right_child = Node(30)
        root.left_child.left_child.right_child = Node(19)
        root.left_child.right_child.right_child = Node(23)
        root.left_child.left_child.right_child.right_child = Node(3)
        root.left_child.left_child.right_child.right_child.right_child = Node(6)
        root.right_child = Node(15)
        root.right_child.left_child = Node(36)
        self.assertEqual('1012251936233615', root.boundaries())

    def test_build_tree(self):
        pre_order = ['A', 'B', 'D', 'E', 'C', 'F']
        in_order = ['D', 'B', 'E', 'A', 'F', 'C']
        root = Node.build_tree(pre_order, in_order)
        self.assertEqual('ABDECF', root.str_pre_order())
        self.assertEqual('DBEAFC', root.str_in_order())

    def test_build_tree_in_level(self):
        level_order = ['A', 'B', 'C', 'D', 'E', 'F']
        in_order = ['D', 'B', 'E', 'A', 'F', 'C']
        root = Node.build_tree_in_level(in_order, level_order)
        self.assertEqual('ABDECF', root.str_pre_order())
        self.assertEqual('DBEAFC', root.str_in_order())

    def test_build_tree_llist(self):
        llist = LinkedList()
        llist.append(10)
        llist.append(12)
        llist.append(15)
        llist.append(25)
        llist.append(30)
        llist.append(36)
        root = Node.build_tree_llist(llist.head)
        self.assertEqual('101225301536', root.str_pre_order())
        self.assertEqual('251230103615', root.str_in_order())

    def test_build_tree_pre_post(self):
        pre_order = ['A', 'B', 'D', 'E', 'C', 'F']
        post_order = ['D', 'E', 'B', 'F', 'C', 'A']
        root = Node.build_tree_pre_post(pre_order, post_order)
        self.assertEqual('ABDECF', root.str_pre_order())
        self.assertEqual('DBEAFC', root.str_in_order())

    def test_build_special_tree(self):
        pre_order = ['A', 'B', 'D', 'E', 'C', 'F', 'G']
        pre_nl = ['N', 'N', 'L', 'L', 'N', 'L', 'L']
        root, index = Node.build_special_tree(pre_order, pre_nl)
        self.assertEqual('ABDECFG', root.str_pre_order())
        self.assertEqual('DBEAFCG', root.str_in_order())

    def test_sorted_lca(self):
        root = Node(50)
        root.insert(13)
        root.insert(21)
        root.insert(27)
        root.insert(76)
        root.insert(2)
        root.insert(44)
        root.insert(51)
        root.insert(6)
        root.insert(9)
        root.insert(11)
        node = root.sorted_lca(11, 44)
        self.assertEqual(node.data, 13)

    def test_lca(self):
        root = Node(50)
        root.insert(13)
        root.insert(21)
        root.insert(27)
        root.insert(76)
        root.insert(2)
        root.insert(44)
        root.insert(51)
        root.insert(6)
        root.insert(9)
        root.insert(11)
        node = root.lca(11, 44)
        self.assertEqual(node.data, 13)

    def test_fast_lca(self):
        root = Node(50)
        root.insert(13)
        root.insert(21)
        root.insert(27)
        root.insert(76)
        root.insert(2)
        root.insert(44)
        root.insert(51)
        root.insert(6)
        root.insert(9)
        root.insert(11)
        node = root.fast_lca(11, 44)
        self.assertEqual(node.data, 13)

    def test_distance(self):
        root = Node(50)
        root.insert(13)
        root.insert(21)
        root.insert(27)
        root.insert(76)
        root.insert(2)
        root.insert(44)
        root.insert(51)
        root.insert(6)
        root.insert(9)
        root.insert(11)
        distance = root.distance(11, 44)
        self.assertEqual(distance, 7)

    def test_sum_tree(self):
        root = Node(50)
        root.insert(13)
        root.insert(21)
        root.insert(27)
        root.insert(76)
        root.insert(2)
        root.insert(44)
        root.insert(51)
        root.insert(6)
        root.insert(9)
        root.insert(11)
        rootb, value = root.get_sum_tree()
        self.assertEqual(rootb.str_in_order(), '262011012071440260051')

    def test_build_from_array(self):
        array = [1, 2, 3, 4, 5, 6, 7]
        root = Node.build_from_array(array)
        self.assertEqual(root.str_in_order(), '1234567')
        self.assertEqual(root.str_pre_order(), '4213657')
        self.assertEqual(root.str_post_order(), '1325764')

    def test_balance(self):
        root = Node(4)
        root.left_child = Node(3)
        root.left_child.left_child = Node(2)
        root.left_child.left_child.left_child = Node(1)
        root.right_child = Node(5)
        root.right_child.right_child = Node(6)
        root.right_child.right_child.right_child = Node(7)
        broot = root.balance()
        self.assertEqual(broot.str_in_order(), '1234567')
        self.assertEqual(broot.str_pre_order(), '4213657')
        self.assertEqual(broot.str_post_order(), '1325764')

