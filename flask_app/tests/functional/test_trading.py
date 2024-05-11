import trading

def test_orders_empty():
	"""
	GIVEN a Flask application configured for testing with no data posted
        WHEN the '/orders' page is requested (GET)
        THEN check that the response is an empty list and code is 200
	"""
	with trading.app.test_client() as test_client:
		response = test_client.get('/orders')
		assert response.status_code == 200
		assert b"[]" in response.data
		
def test_get_order_id_does_not_exist():
	"""
	GIVEN a Flask application configured for testing with no data posted
        WHEN the '/orders/1' page is requested (GET)
        THEN check that the response code is 404
	"""
	with trading.app.test_client() as test_client:
		response = test_client.get('/orders/1')
		assert response.status_code == 404
		
def test_delete_order_id_does_not_exist():
	"""
	GIVEN a Flask application configured for testing with no data posted
        WHEN the '/orders/1' page is deleted (DELETE)
        THEN check that the response code is 404
	"""
	with trading.app.test_client() as test_client:
		response = test_client.delete('/orders/1')
		assert response.status_code == 404
		
def test_post_order():
	"""
	GIVEN a Flask application configured for testing with no data posted
        WHEN the '/orders' page is posted (POST)
        THEN check that the response is 0 id and code is 201
	"""
	with trading.app.test_client() as test_client:
		response = test_client.post('/orders')
		assert response.status_code == 201
		assert b"0" in response.data
		
def test_delete_order_id_that_exists():
	"""
	GIVEN a Flask application configured for testing with no data posted
        WHEN the '/orders' page is posted (POST) and '/orders/0' page is deleted (DELETE)
        THEN check that the response code is 204
	"""
	with trading.app.test_client() as test_client:
		response = test_client.post('/orders')
		response = test_client.delete('/orders/0')
		assert response.status_code == 204
		
def test_orders_non_empty():
	"""
	GIVEN a Flask application configured for testing with no data posted
        WHEN the '/orders' page is posted (POST) and '/orders' page is requested (GET)
        THEN check that the response code is 200 and response contains 0 as the id
	"""
	with trading.app.test_client() as test_client:
		response = test_client.post('/orders')
		response = test_client.get('/orders')
		assert response.status_code == 200
		assert b"0" in response.data
		
def test_get_order_id_that_exists():
	"""
	GIVEN a Flask application configured for testing with no data posted
        WHEN the '/orders' page is posted (POST) 2 times and '/orders/1' page is requested (GET)
        THEN check that the response code is 200 and response has PENDING as status
	"""
	with trading.app.test_client() as test_client:
		response = test_client.post('/orders')
		response = test_client.post('/orders')
		response = test_client.get('/orders/1')
		assert response.status_code == 200
		assert b"PENDING" in response.data
		
		
def test_invalid_method():
	"""
	GIVEN a Flask application configured for testing with no data posted
        WHEN the '/orders' page is deleted (DELETE)
        THEN check that the response code is 405
	"""
	with trading.app.test_client() as test_client:
		response = test_client.delete('/orders')
		assert response.status_code == 405
		assert b"Method Not Allowed" in response.data
