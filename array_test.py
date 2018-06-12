import ds_array
import unittest


class ds_array_tests(unittest.TestCase):

    def test_rotate(self):
        larray = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        ds_array.left_rotate(larray, 3, 9)
        self.assertEqual('4 5 6 7 8 9 1 2 3 ', ds_array.printArray(larray, 9))
