import unittest
import assignment6

class testing(unittest.TestCase):
    def test_prime(self):
        assignment6.SETNUM(5)
        self.assertEqual(assignment6.primeornot(), "is not a prime number")

if __name__ == "__main__":
     unittest.main()
        