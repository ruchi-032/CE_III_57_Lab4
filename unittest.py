import unittest
from greedy_algo import greedy_activity_selector, recursive_greedy_activity_selector

s = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
f = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
expected_a = [0, 3, 7, 10]


class greedyTestCase(unittest.TestCase):
    def test_greedy(self):
        iterative = greedy_activity_selector(s, f)
        self.assertListEqual(iterative, expected_a)
        recur = recursive_greedy_activity_selector(s, f, -1, len(s)) 
        self.assertListEqual(recur, expected_a)
        
if __name__=='__main__':
    unittest.main()