# -*- coding: utf-8 -*-
"""
    fibsvc integration tests
    -----------------------------
"""
import fibsvc
import json
import unittest
import random
from fibsvc import MIN_N, MAX_N
from webtest import TestApp

class FibonacciServiceTestCase(unittest.TestCase):


    def setUp(self):
        self.app = TestApp(fibsvc.app)


    def test_min_max(self):
        self.assertTrue(0 <= MIN_N < MAX_N)
        

    def test_fibsvc_zero(self):
        if MIN_N == 0:
            res = self.app.get("/fibsvc/0")
            self.assertEqual("application/json", res.content_type)
            self.assertEqual(200, res.status_int)
            self.assertTrue("fibonacci" in res.json.keys())

            seq = res.json.values()
            self.assertEqual(1, len(seq))
            self.assertEqual([], seq[0])


    def test_fibsvc_negative(self):
        res = self.app.get("/fibsvc/-10", expect_errors = True)
        self.assertEqual("application/json", res.content_type)
        self.assertEqual(400, res.status_int)

        keys = res.json.keys()
        self.assertTrue("error_type" in keys)
        self.assertTrue("error_message" in keys)
        self.assertTrue("n" in keys)


    def test_fibsvc_smaller_than_min(self):
        res = self.app.get("/fibsvc/%d" % (MIN_N - 1), expect_errors = True)
        self.assertEqual("application/json", res.content_type)
        self.assertEqual(400, res.status_int)

        keys = res.json.keys()
        self.assertTrue("error_type" in keys)
        self.assertTrue("error_message" in keys)
        self.assertTrue("n" in keys)


    def test_fibsvc_larger_than_max(self):
        res = self.app.get("/fibsvc/%d" % (MAX_N + 1), expect_errors = True)
        self.assertEqual("application/json", res.content_type)
        self.assertEqual(400, res.status_int)

        keys = res.json.keys()
        self.assertTrue("error_type" in keys)
        self.assertTrue("error_message" in keys)
        self.assertTrue("n" in keys)
        
        
    def test_fibsvc_no_param(self):
        res = self.app.get("/fibsvc", expect_errors = True)
        self.assertEqual(404, res.status_int)
        
        
    def test_fibsvc_string(self):
        res = self.app.get("/fibsvc/hi", expect_errors = True)
        self.assertEqual(404, res.status_int)
        
        
    def test_fibsvc_float(self):
        res = self.app.get("/fibsvc/2.5", expect_errors = True)
        self.assertEqual(404, res.status_int)
        
        
    def test_fibsvc_post(self):
        res = self.app.post("/fibsvc/10", expect_errors = True)
        self.assertEqual(405, res.status_int)
        
        
    def test_fibsvc_put(self):
        res = self.app.get("/fibsvc/hi", expect_errors = True)
        self.assertEqual(404, res.status_int)
        
        
    def test_fibsvc_delete(self):
        res = self.app.get("/fibsvc/hi", expect_errors = True)
        self.assertEqual(404, res.status_int)
        
        
    def test_fibsvc_valid(self):
        n = random.randint(MIN_N, MAX_N)
        res = self.app.get("/fibsvc/%d" % n)
        self.assertEqual("application/json", res.content_type)
        self.assertEqual(200, res.status_int)
        self.assertTrue("fibonacci" in res.json.keys())

        seq = res.json.values()[0]
        seqlen = len(seq)
        self.assertEqual(n, seqlen)
        
        if n > 2:      
            self.assertEqual(seq[n - 1], seq[n - 3] + seq[n - 2])
        

if __name__ == '__main__':
    unittest.main()
