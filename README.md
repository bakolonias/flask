# flask
Flask app


Install docker on the home machine.
-----------------------------------
For Flask app run from the root directory of the app:

docker build --tag python-flask -f Dockerfile_flask .
docker run -d python-flask

Get the id of the container and find the ip:

docker inspect 8648193b | grep -i ipaddress
            "SecondaryIPAddresses": null,
            "IPAddress": "172.17.0.2",
                    "IPAddress": "172.17.0.2",

Test the app:

curl -i http://172.17.0.2:5000/orders
HTTP/1.1 200 OK
Server: Werkzeug/3.0.3 Python/3.8.17
Date: Fri, 10 May 2024 14:31:01 GMT
Content-Type: application/json
Content-Length: 3
Connection: close

[]
------------------------------------------------------------
For pytest framework run from the root directory of the app:

docker build --tag python-pytest -f Dockerfile_pytest .
docker run -d python-pytest

The id that you will get then you can use it to print the results of the tests:

> docker logs 7d0ef7d7e5b800a26ec34e74b57e14c66a57633da807c167a92d7f2455025a0c
============================= test session starts ==============================
platform linux -- Python 3.8.17, pytest-8.2.0, pluggy-1.5.0
rootdir: /root
collected 8 items

tests/functional/test_trading.py ........                                [100%]

============================== 8 passed in 0.19s ===============================


--------------------------------------------------------------------------------

In the repo, you can also find a picture of the test that was run with jmeter and the results.
