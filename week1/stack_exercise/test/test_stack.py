import unittest
from ..src.stack import Stack


# every test need setup to create a new stack object
class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push_and_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.stack.push(4)

        self.assertEqual(self.stack.peek(), 4)

        self.stack.pop()

        self.assertEqual(self.stack.peek(), 3)

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())





if __name__ == "__main__":
    unittest.main()
