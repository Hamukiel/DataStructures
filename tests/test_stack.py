from src.stack import StackedQueue, Stack, Node
import unittest


class StackTests(unittest.TestCase):

    def test_infix_to_posfix(self):
        stack = Stack()
        exp = "a+b*(c^d-e)^(f+g*h)-i"
        expected = 'abcd^e-fgh*+^*+i-'
        self.assertEqual(expected, stack.infix_to_postfix(exp))

    def test_stacked_queue(self):
        stack = StackedQueue()
        exp = 'abcd'
        for i in exp:
            stack.enqueue(i)
        res = ''
        while not stack.is_empty():
            res = res + stack.dequeue()
        self.assertEqual(exp, res)
