# -*- coding: utf-8 -*-
"""
    Fibonnaci web service unit tests
    -----------------------------
"""
import fibonacci_service
import json
import unittest
from fibonacci_service import MIN_N, MAX_N
from httplib import OK, BAD_REQUEST, NOT_FOUND, METHOD_NOT_ALLOWED
from webtest import TestApp

class FibonacciServiceTestCase(unittest.TestCase):


  def setUp(self):
    self.app = TestApp(fibonacci_service.app)
   
        
  def test_fibsvc_post(self):
    res = self.app.post("/fibsvc/10", expect_errors = True)
    self.assertEqual(METHOD_NOT_ALLOWED, res.status_int)
        
        
  def test_fibsvc_put(self):
    res = self.app.put("/fibsvc/10", expect_errors = True)
    self.assertEqual(METHOD_NOT_ALLOWED, res.status_int)
        
        
  def test_fibsvc_delete(self):
    res = self.app.delete("/fibsvc/10", expect_errors = True)
    self.assertEqual(METHOD_NOT_ALLOWED, res.status_int)

  def test_min_max(self):
    self.assertTrue(0 <= MIN_N < MAX_N)
        

  def test_fibsvc_zero(self):
    if MIN_N == 0:
      res = self.app.get("/fibsvc/0")
      self.assertEqual("application/json", res.content_type)
      self.assertEqual(OK, res.status_int)

      seq = res.json["fibonacci"]
      self.assertEqual(0, len(seq))


  def test_fibsvc_negative(self):
    res = self.app.get("/fibsvc/-10", expect_errors = True)
    self.assertEqual("application/json", res.content_type)
    self.assertEqual(BAD_REQUEST, res.status_int)


  def test_fibsvc_smaller_than_min(self):
    res = self.app.get("/fibsvc/%d" % (MIN_N - 1), expect_errors = True)
    self.assertEqual("application/json", res.content_type)
    self.assertEqual(BAD_REQUEST, res.status_int)


  def test_fibsvc_larger_than_max(self):
    res = self.app.get("/fibsvc/%d" % (MAX_N + 1), expect_errors = True)
    self.assertEqual("application/json", res.content_type)
    self.assertEqual(BAD_REQUEST, res.status_int)
       

  def test_fibsvc_no_param(self):
    res = self.app.get("/fibsvc", expect_errors = True)
    self.assertEqual("application/json", res.content_type)
    self.assertEqual(NOT_FOUND, res.status_int)
        
        
  def test_fibsvc_string(self):
    res = self.app.get("/fibsvc/hi", expect_errors = True)
    self.assertEqual("application/json", res.content_type)
    self.assertEqual(NOT_FOUND, res.status_int)


  def test_fibsvc_long_url(self):
    res = self.app.get("/fibsvc/foo/bar", expect_errors = True)
    self.assertEqual("application/json", res.content_type)
    self.assertEqual(NOT_FOUND, res.status_int)
        

  def test_fibsvc_float(self):
    res = self.app.get("/fibsvc/2.5", expect_errors = True)
    self.assertEqual("application/json", res.content_type)
    self.assertEqual(NOT_FOUND, res.status_int)
        
        
  def test_fibsvc_valid(self):
    n = 500
    res = self.app.get("/fibsvc/%d" % n)
    self.assertEqual("application/json", res.content_type)
    self.assertEqual(OK, res.status_int)

    seq = res.json["fibonacci"]
    seqlen = len(seq)
    self.assertEqual(n, seqlen)
    
    self.assertEqual(seq[n - 1], seq[n - 3] + seq[n - 2])
        

if __name__ == '__main__':
    unittest.main()
