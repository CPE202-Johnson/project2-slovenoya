# Start of unittest - add to completely test functions in exp_eval

import unittest
from exp_eval import *
from stack_array import Stack

class test_expressions(unittest.TestCase):

    def test_postfix_eval_01(self):
        self.assertAlmostEqual(postfix_eval("3 5 +"), 8)

    def test_postfix_eval_05(self):
        self.assertAlmostEqual(postfix_eval("3 5 -"), 3-5)

    def test_postfix_eval_06(self):
        self.assertAlmostEqual(postfix_eval("3 5 *"), 15)

    def test_postfix_eval_07(self):
        self.assertAlmostEqual(postfix_eval("3 5 /"), 3/5)

    def test_postfix_eval_09(self):
        with self.assertRaises(ValueError):
            postfix_eval("3 0 /")

    def test_postfix_eval_08(self):
        self.assertAlmostEqual(postfix_eval("3 4 /**"), 3**4)

    def test_postfix_eval_02(self):
        try:
            postfix_eval("rua rua rua")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval_03(self):
        try:
            postfix_eval("4 4 + 5 + +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_04(self):
        try:
            postfix_eval("1 2 3 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")

    def test_prefix_convert(self):
        self.assertEqual(prefix_to_postfix("+ 3 / * 4 2 >> - 1 5 << 2 3"), "3 4 2 * 1 5 - 2 3 << >> / +")

if __name__ == "__main__":
    unittest.main()
