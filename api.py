# api/function.py
import json

def handler(request):
    if request.method == 'POST':
        # Get the input data from the request
        data = json.loads(request.body.decode('utf-8'))
        input_value = data.get('input', '')
        
        # Perform any operation on the input (e.g., reverse the input)
        result = input_value[::-1]  # Example: Reverse the input string

        return {
            "statusCode": 200,
            "body": json.dumps({"result": result})
        }
    return {
        "statusCode": 405,
        "body": json.dumps({"error": "Method not allowed"})
    }
