import unittest

from stack_array import Stack

class TestPro2(unittest.TestCase):
    
    def test1(self):
        stack = Stack(5)
        self.assertTrue(stack.is_empty())
        with self.assertRaises(IndexError):
            stack.pop()
        with self.assertRaises(IndexError):
            stack.peek()

        stack.push(3)
        stack.push(4)
        stack.push(5)
        stack.push(6)
        stack.push(7)
        self.assertTrue(stack.is_full())
        with self.assertRaises(IndexError):
            stack.push(2)

        self.assertEqual(7, stack.pop())
        self.assertFalse(stack.is_full())

        stack.push(1)
        self.assertEqual(1, stack.peek())




if __name__ == '__main__': 
    unittest.main()