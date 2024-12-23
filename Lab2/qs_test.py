import unittest
from Quicksort import quick_sort

class TestQuickSort(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ([3,2,1,5,4], [1,2,3,4,5]),#General case
            ([1,2,3,4,5], [1,2,3,4,5]),#Already sorted
            ([5,4,3,2,1], [1,2,3,4,5]), #reverse order
            ([1,1,1,1,1], [1,1,1,1,1]),#same elements
            ([1],[1]),#single element
            ([],[])#no elements
        ]

    def test_quick_sort(self):
        for input_array, expected_output in self.test_cases:
            with self.subTest(input_array = input_array):
                quick_sort(input_array, 0, len(input_array)-1)
                self.assertEqual(input_array, expected_output)

if __name__ == '__main__':
    unittest.main()