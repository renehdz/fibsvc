fibsvc
======

A Fibonacci RESTful web service.


## Requirements ##
* Python 2.7.5+
* Bottle 0.12.8
* WebTest 2.0.18

### Install requirements ###

```
$ pip install bottle==0.12.8
$ pip install WebTest==2.0.18
```

### Run logic unit test ###

```
$ python fibonacci_unit_test.py
```

### Run web service unit test ###

```
$ python fibonacci_service_unit_test.py
```

### Run web service ###

```
$ python fibonacci_service.py
```

### Run console application ###

```
$ python fibonacci.py
```

### Using fibsvc ####

Assuming your local development is accessible via `http://localhost:8080/`
you can consume the web service by sending an HTTP GET request like the one below
(where <i>n</i> is zero or a positive integer):

```
http://localhost:8080/fibsvc/n
```
