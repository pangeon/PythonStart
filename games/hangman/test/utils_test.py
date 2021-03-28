import unittest

import sys
sys.path.insert(
    1, 'C:\\Users\\ceche\\PythonProjects\\PythonStart\\games\\hangman\\')

print(sys.path[1])

import utils

class TestUtils(unittest.TestCase):

    def test_index_of_set(self):
        self.assertEqual(utils.index_of_set(
            {"b", "c", "a", "d"}, 0), "a", "Should be a")
        self.assertEqual(utils.index_of_set(
            {"a", "b", "c", "d"}, 1), "b", "Should be b")
        self.assertEqual(utils.index_of_set(
            {"b", "a", "c", "d"}, 2), "c", "Should be c")
        self.assertEqual(utils.index_of_set(
            {"c", "d", "b", "a"}, 3), "d", "Should be d")

        self.assertEqual(utils.index_of_set(
            {"forest", "guy", "lemon", "hero"}, 0), "forest", "Should be forest")
        self.assertEqual(utils.index_of_set(
            {"forest", "guy", "lemon", "hero"}, 3), "lemon", "Should be lemon")

if __name__ == '__main__':
    unittest.main()