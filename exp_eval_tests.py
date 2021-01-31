# Start of unittest - add to completely test functions in exp_eval

import unittest
from exp_eval import *
from stack_array import Stack

class test_expressions(unittest.TestCase):

    def test_toStack(self):
        stack = Stack(7)
        stack.push("df")
        stack.push("kld")
        stack.push(0)
        stack.push(3)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.toStack("3 2 1 3 0 kld df"), stack)


    # def test_postfix_eval_01(self):
    #     self.assertAlmostEqual(postfix_eval("3 5 +"), 8)

    # def test_postfix_eval_02(self):
    #     try:
    #         postfix_eval("blah")
    #         self.fail()
    #     except PostfixFormatException as e:
    #         self.assertEqual(str(e), "Invalid token")

    # def test_postfix_eval_03(self):
    #     try:
    #         postfix_eval("4 +")
    #         self.fail()
    #     except PostfixFormatException as e:
    #         self.assertEqual(str(e), "Insufficient operands")

    # def test_postfix_eval_04(self):
    #     try:
    #         postfix_eval("1 2 3 +")
    #         self.fail()
    #     except PostfixFormatException as e:
    #         self.assertEqual(str(e), "Too many operands")

if __name__ == "__main__":
    unittest.main()
