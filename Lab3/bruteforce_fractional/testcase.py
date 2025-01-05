import unittest
from main import bruteforce_fractional_knapsack

class TestBruteForce_01(unittest.TestCase):
    def test_basicCase(self):
        p = [1,4,5,7]
        w = [1,3,4,5]
        m = 10
        result = bruteforce_fractional_knapsack(p,w,m)
        self.assertAlmostEqual(result,13.5)
    
    def test_allItemsFit(self):
        p = [10,20,30]
        w=[1,2,3]
        m = 10
        result = bruteforce_fractional_knapsack(p,w,m)
        self.assertAlmostEqual(result,60)

    def test_lowCapacity(self):
        p = [2,3,5]
        w = [4,5,6]
        m = 3
        result = bruteforce_fractional_knapsack(p,w,m)
        self.assertEqual(result,2.5)

    def test_singleItem(self):
        p = [100]
        w = [50]
        m = 40
        result = bruteforce_fractional_knapsack(p,w,m)
        self.assertEqual(result, 80)

    def test_noItems(self):
        p = []
        w =[]
        m = 10
        result = bruteforce_fractional_knapsack(p,w,m)
        self.assertEqual(result,0)


if __name__ == "__main__":
    unittest.main()   