# functions.py

import json

def handle_get():
    # Logic to handle GET request
    response_data = {"message": "Hello from the Python API!"}
    return response_data

def handle_post(data):
    # Logic to handle POST request with incoming data
    response_data = {"received": data}
    return response_data
