fibsvc
======

A Fibonacci RESTful web service.


## Requirements ##
* Python 2.7.5+
* Bottle 0.11.6
* WebTest 2.0.10

### Install requirements ###

```
$ pip install bottle-0.11.6
$ pip install WebTest
```

### Run unit test ###

```
$ python fibsvc_unittest.py
```

### Run integration test ###

```
$ python fibsvc_integrationtest.py
```

### Run web service ###

```
$ python fibsvc.py
```

### Using fibsvc ####

Assuming your local development is accessible via `http://localhost:8080/`
you can consume the web service by sending a get request like the one below
(where <i>n</i> is zero or a positive integer)

```
http://localhost:8080/fibsvc/n
```
