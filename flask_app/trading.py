import time
import random
from flask import Flask, jsonify, request, abort

orders_list_of_dicts = []

app = Flask(__name__)

@app.route('/orders', methods=['GET', 'POST'])
def orders():
	"""
	Returns the list of orders (200) or the id of the new order (201), 
	depending on the method (GET, POST)

            Parameters:

            Returns:
                    list of dictionaries with the orders with code 200 or
                    string of order id with code 201
	"""
	delay_time = random.uniform(0.1, 1)
	if request.method == 'GET':
		time.sleep(delay_time)
		return orders_list_of_dicts, 200
	elif request.method == 'POST':
		temp_dict = {}
		temp_dict['id'] = len(orders_list_of_dicts)
		temp_dict['status'] = "PENDING"
		orders_list_of_dicts.append(temp_dict)
		time.sleep(delay_time)
		return str(temp_dict['id']), 201


@app.route('/orders/<order_id>', methods=['GET', 'DELETE'])
def get_order_status(order_id):
	"""
	Returns the status of order (200) and 404 if it does not exist or
	or 204 depending on the method (GET, DELETE) 

            Parameters:
		     order_id - The id of the order to be found or deleted
            Returns:
                    string of status of the order with code 200, 404 if it does not exist 
                    or 204 if the order was cancelled successfully, 404 if it does not exist
        """
	delay_time = random.uniform(0.1, 1)
	if request.method == 'GET':
		if len(orders_list_of_dicts) >= int(order_id):
			time.sleep(delay_time)
			return orders_list_of_dicts[int(order_id)]['status'], 200
		else:
			time.sleep(delay_time)
			abort(404)
	elif request.method == 'DELETE':
		if len(orders_list_of_dicts) > int(order_id):
			orders_list_of_dicts[int(order_id)]['status'] = "CANCELLED"
			time.sleep(delay_time)
			return '', 204
		else:
			time.sleep(delay_time)
			abort(404)



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
