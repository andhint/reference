import unittest

# 1) Put problem into own words
# 2) Define input/output types
# 3) Define test/edge cases
# 4) Consider what data structures to use
# 5) Psuedocode
# 5) Code

# function to test here
def add(num1: int, num2: int) -> int:
    return num1 + num2




# testing
class TestCalc(unittest.TestCase):

    def test_add(self):
        """
        Must be of form `test_{function_name}` for unittest to recognize
        """
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

if __name__ == '__main__':
    unittest.main()