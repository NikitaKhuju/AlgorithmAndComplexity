import unittest
from BinarySearch import BinarySearch

class test(unittest.TestCase):
    def test_target_found(self):
        array = [10,20,30,40,50]
        target = 40
        result = BinarySearch(array, target)
        self.assertEqual(result,3)
    def test_target_not_found(self):
        array = [1,2,3,4,5,6,7]
        target = 9
        result = BinarySearch(array,target)
        self.assertEqual(result, -1)
    def test_empty(self):
        in_array = []
        in_target = 6
        result = BinarySearch(in_array, in_target)
        self.assertEqual(result, -1)
    def test_one_element(self):
        in_array= [3]
        in_target = 3
        result = BinarySearch(in_array, in_target)
        self.assertEqual(result,0)
    def test_duplicate(self):
        in_array = [1,2,3,2,4,5]
        in_target=2
        result = BinarySearch(in_array, in_target)
        self.assertEqual(result,1)


if __name__ == "__main__":
    unittest.main()