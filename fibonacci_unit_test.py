# -*- coding: utf-8 -*-
"""
    Fibonacci sequence unit tests
    -----------------------------
"""
import unittest
from fibonacci import fibonacci_sequence

class TestFibonacciSequence(unittest.TestCase):


    def test_zero(self):
        seq = fibonacci_sequence(0)
        self.assertEqual(0, len(seq))


    def test_negative(self):
        seq = fibonacci_sequence(-10)
        self.assertEqual(0, len(seq))
        

    def test_float(self):
        self.assertRaises(TypeError, fibonacci_sequence, 2.5)


    def test_string(self):
        self.assertRaises(TypeError, fibonacci_sequence, "2")


    def test_length(self):
        seq = fibonacci_sequence(123)
        self.assertEqual(123, len(seq))


    def test_sequence_start(self):
        seq = fibonacci_sequence(3)        
        self.assertEqual(0, seq[0])
        self.assertEqual(1, seq[1])
        self.assertEqual(1, seq[2])


    def test_sequence_end(self):
        seq = fibonacci_sequence(500)
        self.assertEqual(seq[499], seq[498] + seq[497])


if __name__ == '__main__':
    unittest.main()
