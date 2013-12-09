# -*- coding: utf-8 -*-
"""
    fibsvc
    -----------------
    A Fibonacci RESTful web service.
"""
import bottle
from bottle import route, run, response
from httplib import BAD_REQUEST


MIN_N = 0
MAX_N = 1000


app = bottle.Bottle()


def fib(n):
    """Returns a list of n Fibonacci numbers."""
    result = []
    a, b = 0, 1
    for i in range(n):
        result.append(a)
        a, b = b, a+b
    return result


@app.get('/fibsvc/<n:int>')
def fibsvc(n):
    if MIN_N <= n <= MAX_N:
        return { 
            "fibonacci" : fib(n) 
        }  
    response.status = BAD_REQUEST
    return {
        "error_type" : "Invalid argument", 
        "error_message" : "n must be an integer between %d and %d" % (MIN_N, MAX_N),
        "n" : n
    }     


if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True)
