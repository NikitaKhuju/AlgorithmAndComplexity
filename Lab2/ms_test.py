import unittest
from MergeSort import merge_sort

class TestMergeSort(unittest.TestCase):
    def setUp(self):
        self.testcases = [
        ([3,6,2,8,5,1],[1,2,3,5,6,8]),
        ([1,2,3,4,5],[1,2,3,4,5]),
        ([5,4,3,2,1],[1,2,3,4,5]),
        ([1,1,1,1,1], [1,1,1,1,1]),
        ([1],[1]),
        ([],[]),
        ([-3,-2,1,-5,4],[-5,-3,-2,1,4]),
        ([3.1,2.2,5.5,4.3,1.7],[1.7,2.2,3.1,4.3,5.5]),
        ([2,5,3,3,5,2],[2,2,3,3,5,5])
        ]

    def test_merge_sort(self):
        for input_array, expected_output in self.testcases:
            with self.subTest(input_array = input_array):
                merge_sort(input_array, 0, len(input_array)-1)
                self.assertEqual(input_array,expected_output)

if __name__ == '__main__':
    unittest.main()