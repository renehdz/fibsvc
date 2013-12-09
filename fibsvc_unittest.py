# -*- coding: utf-8 -*-
"""
    Fibonacci sequence unit tests
    -----------------------------
"""
import random
import unittest
from fibsvc import fib

class TestFibonacciSequence(unittest.TestCase):


    def test_zero(self):
        seq = fib(0)
        self.assertEqual(0, len(seq))


    def test_negative(self):
        seq = fib(-10)
        self.assertEqual(0, len(seq))


    def test_length(self):
        n = random.randint(1, 1000)
        seq = fib(n)
        self.assertEqual(n, len(seq))


    def test_sequence_start(self):
        n = random.randint(3, 1000)
        seq = fib(n)        
        self.assertEqual(0, seq[0])
        self.assertEqual(1, seq[1])
        self.assertEqual(1, seq[2])
        
        i = random.randint(2,n-1)
        self.assertEqual(seq[i], seq[i-2] + seq[i-1])


    def test_sequence_middle(self):
        n = random.randint(3, 1000)
        seq = fib(n)
        i = random.randint(2,n-1)
        self.assertEqual(seq[i], seq[i-2] + seq[i-1])


    def test_sequence_end(self):
        n = random.randint(3, 1000)
        seq = fib(n)  
        self.assertEqual(seq[n - 1], seq[n - 3] + seq[n - 2])
        

    def test_float(self):
        self.assertRaises(TypeError, fib, 2.5)


    def test_string(self):
        self.assertRaises(TypeError, fib, "2")


if __name__ == '__main__':
    unittest.main()
