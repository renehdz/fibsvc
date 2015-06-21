# -*- coding: utf-8 -*-
"""
    fibsvc
    -----------------
    A Fibonacci RESTful web service.
"""
import json
import bottle
from bottle import get, response, route, run
from httplib import OK, BAD_REQUEST, NOT_IMPLEMENTED
from fibonacci import fibonacci_sequence


MIN_N = 0
MAX_N = 1000


app = bottle.Bottle()


@app.get("/fibsvc/<n:int>")
def fibsvc(n):
  response.headers["Content-Type"] = "application/json"
  if MIN_N <= n <= MAX_N:
    response.status = OK
    return json.dumps(fibonacci_sequence(n))
  else:
    response.status = BAD_REQUEST
    result =  {"invalidArgument": {
      "message" : "n must be an integer between %d and %d" % (MIN_N, MAX_N),
      "n" : n}}
    return json.dumps(result)


@app.route("/")
@app.route("/<url:re:.+>")
def not_found(url):
    response.headers["Content-Type"] = "application/json"
    response.status = NOT_IMPLEMENTED
    result = {"notImplemented": {
       "message": "The server does not support this feature"}}
    return json.dumps(result)


if __name__ == "__main__":
    run(app, host="localhost", port=8080, debug=True)
