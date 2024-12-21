import unittest
from LinearSearch import LinearSearch

class test(unittest.TestCase):
    def test_right(self):
        in_array = [9,8,3,4,5]
        in_target = 3
        result = LinearSearch(in_array, in_target)
        self.assertEqual(result,2)
    def test_wrong(self):
        in_array = [1,2,3,4,5]
        in_target = 6
        result = LinearSearch(in_array, in_target)
        self.assertEqual(result, -1)
    def test_empty(self):
        in_array = []
        in_target = 6
        result = LinearSearch(in_array, in_target)
        self.assertEqual(result, -1)
    def test_one_element(self):
        in_array= [3]
        in_target = 3
        result = LinearSearch(in_array, in_target)
        self.assertEqual(result,0)
    def test_duplicate(self):
        in_array = [1,2,3,2,4,5]
        in_target=2
        result = LinearSearch(in_array, in_target)
        self.assertEqual(result,1)

if __name__ == "__main__":
    unittest.main()
    