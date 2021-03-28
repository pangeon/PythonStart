
import unittest
import sys
sys.path.insert(
    1, 'C:\\Users\\ceche\\PythonProjects\\PythonStart\\games\\hangman\\')

from validate import Validator

class TestValidator(unittest.TestCase):

    def test_object_create(self):
        Validator = Validator()


if __name__ == '__main__':
    unittest.main()

obj = validate.Validator("Kamil", 35)
print(obj.name)
