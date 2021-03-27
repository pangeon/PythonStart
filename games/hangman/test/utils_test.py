import sys
sys.path.insert(1, 'C:\\Users\\ceche\\PythonProjects\\PythonStart\\games\\hangman\\')

import utils
import unittest

print(sys.path[1])

class TestUtils(unittest.TestCase):

    def test_index_of_set(self):
        self.assertEqual(utils.index_of_set({"a", "b", "c"}, 1), "a", "Should be a")
        self.assertEqual(utils.index_of_set({"a", "b", "c"}, 2), "a", "Should be b")

if __name__ == '__main__':
    unittest.main()

print("--- END TESTS ---")
        


